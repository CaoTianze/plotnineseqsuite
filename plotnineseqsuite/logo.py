from functools import reduce
from math import floor, log, ceil
from typing import Union, List, Dict

from numpy import ndarray, array, zeros, sum, apply_along_axis, log2
from pandas import merge, DataFrame, concat
from pandas.core.dtypes.common import is_numeric_dtype
from plotnine import aes, geom_polygon, scale_x_continuous
from plotnine.scales import scale_fill_gradient, scale_fill_manual
from plotnine.guides import guides
from plotnine.labels import xlab, ylab

from plotnineseqsuite.col_schemes import get_col_scheme
from plotnineseqsuite.font import get_font
from plotnineseqsuite.common import find_namespace, new_range, letter_matrix


class geom_logo:
    def __init__(self, data: Union[List[str], ndarray, Dict] = None, method: str = 'bits', seq_type: str = 'AUTO',
                 namespace: List[str] = None,
                 font: str = 'roboto_medium', stack_width: float = 0.95, rev_stack_order: bool = False,
                 col_scheme: Union[DataFrame, str] = 'AUTO',
                 low_col: str = 'black', high_col: str = 'yellow', na_col: str = '#333333',
                 **kwargs):
        if stack_width > 1 or stack_width <= 0:
            raise Exception('"stack_width" must be between 0 and 1')
        if data is None:
            raise Exception('Missing "data" parameter!')
        if namespace is not None:
            seq_type = 'OTHER'
        if method not in {'bits', 'probability', 'custom'}:
            raise Exception("method must be one of 'bits' or 'probability', or 'custom'")
        if seq_type not in {'OTHER', 'AUTO', 'AA', 'DNA', 'RNA'}:
            raise Exception("seq_type must be one of 'OTHER' or 'AUTO', or 'AA', or 'DNA', or 'RNA'")
        if type(data) == list or type(data) == ndarray:
            data = {1: data}
        lvls = data.keys()
        data_sp = list(map(lambda x: self.__logo_data(data[x], method=method, stack_width=stack_width,
                                                      rev_stack_order=rev_stack_order, seq_group=x,
                                                      seq_type=seq_type,
                                                      font=font, namespace=namespace), lvls))
        seq_type = data_sp[0]['seq_type']
        data = reduce(lambda x, y: concat([x, y]), map(lambda x: x['logo_data'], data_sp))
        if type(col_scheme) is str:
            cs_dict = get_col_scheme(col_scheme, seq_type)
        else:
            cs_dict = col_scheme
        legend_title = cs_dict['name']
        data = merge(data, cs_dict['cs'], how='left')
        data = data.sort_values(by='order').reset_index(drop=True)

        colscale_gradient = True if is_numeric_dtype(cs_dict['cs']['group']) else False

        if colscale_gradient:
            colscale_opts = scale_fill_gradient(low=low_col, high=high_col, name=legend_title, na_value=na_col)
        else:
            tmp = cs_dict['cs'].drop_duplicates(subset=['group']).dropna(subset=['group'])
            col_map = {}
            for item in map(lambda x, y: {x: y}, tmp['group'], tmp['col']):
                col_map.update(item)
            colscale_opts = scale_fill_manual(values=col_map, name=legend_title, na_value=na_col)
        if method == 'custom':
            y_lab = ''
        else:
            y_lab = method.capitalize()

        data['group_by'] = data.apply(lambda x: '{}.{}.{}'.format(x['seq_group'], x['letter'], x['position']), axis=1)
        self.data = data
        self.layer = geom_polygon(data=data, mapping=aes(x='x', y='y', fill='group', group='group_by'), **kwargs)
        self.scale_x_continuous = scale_x_continuous(breaks=lambda x: range(floor(x[0]), ceil(x[1])), expand=(0,0))
        self.ylab = ylab(y_lab)
        self.xlab = xlab('')
        self.colscale_opts = colscale_opts

    def __logo_data(self, seqs, font, method='bits', stack_width=0.95, rev_stack_order=False, seq_group=1,
                    seq_type='AUTO',
                    namespace=None):
        font_df = get_font(font)
        if method == 'bits':
            height_dict = self.__bits_method(seqs, reverse=rev_stack_order, seq_type=seq_type, namespace=namespace)
            hh = height_dict['height_df']
            seq_type = height_dict['seq_type']
        elif method == 'probability':
            height_dict = self.__probability_method(seqs, reverse=rev_stack_order, seq_type=seq_type, namespace=namespace)
            hh = height_dict['height_df']
            seq_type = height_dict['seq_type']
        elif method == 'custom':
            if seq_type == 'AUTO' and namespace is None:
                raise Exception("seq_type can not be 'AUTO', when namespace is None.")
            if seq_type != 'OTHER':
                namespace = find_namespace(seq_type=seq_type)['namespace']
            hh = self.__matrix_to_heights(seqs, namespace, reverse=rev_stack_order)
        else:
            raise Exception('Invalid method!')
        ff = merge(font_df, hh, on='letter')
        x_pad = stack_width / 2
        ff['x'] = new_range(ff['x'], ff['position'] - x_pad, ff['position'] + x_pad)
        ff['y'] = new_range(ff['y'], ff['y0'], ff['y1'])
        ff = ff[['x', 'y', 'letter', 'position', 'order']]
        ff['seq_group'] = seq_group

        return {'seq_type': seq_type,
                'logo_data': ff}

    def __radd__(self, gg):
        gg = gg + [self.layer, self.scale_x_continuous, self.ylab, self.xlab, self.colscale_opts]
        return gg


    def __bits_method(self, seqs: Union[List[str], ndarray], reverse: bool, seq_type: str, namespace: List[str]) -> Dict:
        pfm_dict = self.__make_PFM(seqs, seq_type, namespace)
        ic = pfm_dict['bits']
        if (ic == 0).all():
            print(
                'All positions have zero information content perhaps due to too few input sequences. Setting all information content to 2.')
            ic = ic + 2
        mat = pfm_dict['pfm'] * ic
        df = self.__matrix_to_heights(mat=mat, namespace=pfm_dict['namespace'], reverse=reverse)
        return {'seq_type': pfm_dict['seq_type'],
                'height_df': df}


    def __probability_method(self, seqs: Union[List[str], ndarray], reverse: bool, seq_type: str, namespace: List[str]) -> Dict:
        pfm_dict = self.__make_PFM(seqs, seq_type, namespace)
        df = self.__matrix_to_heights(mat=pfm_dict['pfm'], namespace=pfm_dict['namespace'], reverse=reverse)
        return {'seq_type': pfm_dict['seq_type'],
                'height_df': df}


    def __matrix_to_heights(self, mat: ndarray, namespace: List[str], reverse=False) -> DataFrame:
        def add_df(p):
            position_pfm = mat[:, p]
            position_pfm_named = list(map(lambda x, y: (y, x), position_pfm, namespace))
            pos = filter(lambda x: x[1] >= 0, position_pfm_named)
            neg = filter(lambda x: x[1] < 0, position_pfm_named)
            pos = sorted(pos, key=lambda x: x[1], reverse=reverse)
            neg = sorted(neg, key=lambda x: x[1], reverse=not reverse)
            pos_cumsum = []
            neg_cumsum = []
            for i in range(len(pos)):
                if i == 0:
                    tmp = pos[i][1]
                else:
                    tmp = tmp + pos[i][1]
                pos_cumsum.append((pos[i][0], tmp))
            for i in range(len(neg)):
                if i == 0:
                    tmp = neg[i][1]
                else:
                    tmp = tmp + neg[i][1]
                neg_cumsum.append((neg[i][0], tmp))
            df_pos = df_neg = None
            if len(pos_cumsum) > 0:
                letter = list(map(lambda x: x[0], pos_cumsum))
                position = [p + 1] * len(letter)
                y1 = list(map(lambda x: x[1], pos_cumsum))
                y0 = [0] + y1[0:len(y1) - 1]
                df_pos = DataFrame(data={
                    'letter': letter,
                    'position': position,
                    'y0': y0,
                    'y1': y1})
            if len(neg_cumsum) > 0:
                letter = list(map(lambda x: x[0], neg_cumsum))
                position = [p + 1] * len(letter)
                y0 = list(map(lambda x: x[1], neg_cumsum))
                y1 = [0] + y0[0:len(y0) - 1]
                df_neg = DataFrame(data={
                    'letter': letter,
                    'position': position,
                    'y0': y0,
                    'y1': y1})
            return concat([df_pos, df_neg])

        height_df = reduce(lambda x, y: concat([x, y]), map(add_df, range(mat.shape[1])))
        space_factor = 0.004
        y_pad = max(height_df['y1']) * space_factor
        height_df['y0'] = height_df['y0'] + y_pad
        height_df = height_df[height_df.y1 > height_df.y0].reset_index(drop=True)
        if height_df['position'].min() != 1:
            height_df = concat([height_df, DataFrame([[height_df['letter'][0], 1, 0, 0]],
                                                     columns=['letter', 'position', 'y0', 'y1'])]).reset_index(drop=True)
        if height_df['position'].max() != mat.shape[1]:
            height_df = concat([height_df, DataFrame([[height_df['letter'][0], mat.shape[1], 0, 0]],
                                                     columns=['letter', 'position', 'y0', 'y1'])]).reset_index(drop=True)
        return height_df


    def __make_PFM(self, seqs: Union[List[str], ndarray], seq_type: str = 'AUTO', namespace: List[str] = None) -> dict:
        def add_PFM_col(letter_col):
            letter_count = {}
            for x in letter_col:
                if x in letter_count.keys():
                    letter_count[x] = letter_count[x] + 1
                else:
                    letter_count[x] = 1
            PFM_col = array(zeros(len(namespace)))
            for i in range(len(namespace)):
                if namespace[i] in letter_count.keys():
                    PFM_col[i] = letter_count[namespace[i]]
            return PFM_col / sum(PFM_col)

        if type(seqs) is ndarray:
            nseqs = None
            if seq_type == 'AUTO' and namespace is None:
                raise Exception("seq_type can not be 'AUTO', when namespace is None.")
            if seq_type != 'OTHER':
                namespace_dict = find_namespace(seq_type=seq_type)
                namespace = namespace_dict['namespace']
                seq_type = namespace_dict['seq_type']
            pfm_mat = apply_along_axis(lambda x : x/sum(x), 0, seqs)
        else:
            nseqs = len(seqs)
            letter_mat = letter_matrix(seqs)
            ns = find_namespace(letter_mat, seq_type, namespace=namespace)
            namespace = ns['namespace']
            seq_type = ns['seq_type']
            pfm_mat = apply_along_axis(add_PFM_col, 0, letter_mat)
        N = len(namespace)
        bits = self.__compute_bits(pfm_mat, N, nseqs)
        return {'bits': bits, 'namespace': namespace, 'seq_type': seq_type, 'pfm': pfm_mat}


    def __compute_bits(slef, pfm: ndarray, N: int = 4, Nseqs: ndarray = None) -> ndarray:
        pfm = pfm.copy()
        pfm[pfm == 0] = 1
        log2_pfm = log2(pfm)
        H_i = - apply_along_axis(lambda x: sum(x), 0, pfm * log2_pfm)
        e_n = 0
        if Nseqs is not None:
            e_n = (1 / log(2)) * (N - 1) / (2 * Nseqs)
        R_i = log2(N) - (H_i + e_n)
        R_i = map(lambda x: max(x, 0), R_i.tolist())
        return array(list(R_i))
