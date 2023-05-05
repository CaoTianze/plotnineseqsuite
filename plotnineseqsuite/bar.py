from functools import reduce
from math import floor, ceil
from typing import List, Dict, Union

from numpy import ndarray, array, zeros, apply_along_axis
from pandas import merge, DataFrame, concat
from pandas.core.dtypes.common import is_numeric_dtype
from plotnine import scale_fill_gradient, scale_fill_manual, aes, geom_tile, \
    scale_x_continuous, scale_y_continuous, geom_polygon, xlab, ylab, guides

from plotnineseqsuite.col_schemes import get_col_scheme
from plotnineseqsuite.font import get_font
from plotnineseqsuite.common import find_namespace, letter_matrix, new_range


class geom_seqBar:
    def __init__(self, data: Union[List[str], ndarray, Dict] = None, seq_type: str = 'AUTO',
                 namespace: List[str] = None,
                 font: str = 'roboto_medium', stack_width: float = 0.75, bar_col_scheme: Union[DataFrame, str] = 'AUTO',
                 font_col: str = '#808080',
                 low_col: str = 'black', high_col: str = 'yellow', na_col: str = '#333333',
                 **kwargs):
        if stack_width > 1 or stack_width <= 0:
            raise Exception('"stack_width" must be between 0 and 1')
        if data is None:
            raise Exception('Missing "data" parameter!')
        if namespace is not None:
            seq_type = 'OTHER'
        if seq_type not in {'OTHER', 'AUTO', 'AA', 'DNA', 'RNA'}:
            raise Exception("seq_type must be one of 'OTHER' or 'AUTO', or 'AA', or 'DNA', or 'RNA'")
        if type(data) == list or type(data) == ndarray:
            data = {1: data}
        lvls = data.keys()
        data_sp = list(map(lambda x: self.__bar_data(data[x], stack_width=stack_width,
                                                     seq_group=x,
                                                     seq_type=seq_type,
                                                     font=font, namespace=namespace), lvls))
        seq_type = data_sp[0]['seq_type']
        bar_data = reduce(lambda x, y: concat([x, y]), map(lambda x: x['bar_data'], data_sp))
        if font is not None:
            letter_data = reduce(lambda x, y: concat([x, y]), map(lambda x: x['letter_data'], data_sp))
        if type(bar_col_scheme) is str:
            bar_cs_dict = get_col_scheme(bar_col_scheme, seq_type)
        else:
            bar_cs_dict = bar_col_scheme
        legend_title = bar_cs_dict['name']
        bar_data = merge(bar_data, bar_cs_dict['cs'], how='left')
        if font is not None:
            letter_data = letter_data.sort_values(by='order').reset_index(drop=True)
            letter_data['group_by'] = letter_data.apply(
                lambda x: '{}.{}.{}'.format(x['seq_group'], x['letter'], x['position']), axis=1)
            self.letter_data = letter_data
            self.letter_layer = geom_polygon(data=letter_data, mapping=aes(x='x', y='y', group='group_by'),
                                             fill=font_col, **kwargs)
        colscale_gradient = True if is_numeric_dtype(bar_cs_dict['cs']['group']) else False
        if colscale_gradient:
            colscale_opts = scale_fill_gradient(low=low_col, high=high_col, name=legend_title, na_value=na_col)
        else:
            tmp = bar_cs_dict['cs'].drop_duplicates(subset=['group']).dropna(subset=['group'])
            col_map = {}
            for item in map(lambda x, y: {x: y}, tmp['group'], tmp['col']):
                col_map.update(item)
            colscale_opts = scale_fill_manual(values=col_map, name=legend_title, na_value=na_col)
        self.bar_data = bar_data
        self.bar_layer = geom_tile(data=bar_data,
                                   mapping=aes(x='x', y='y', width='width', height='height', fill='group'), **kwargs)
        if font is None:
            self.letter_data = None
            self.letter_layer = None
        self.scale_x_continuous = scale_x_continuous(breaks=lambda x: range(floor(x[0]), ceil(x[1])), expand=(0,0))
        self.scale_y_continuous = scale_y_continuous(breaks=[0,1])
        self.ylab = ylab('Seq Bar')
        self.xlab = xlab('')
        self.colscale_opts = colscale_opts

    def __bar_data(self, seqs, font, stack_width=0.95, seq_group=1,
                   seq_type='AUTO', namespace=None):
        frequency_dict = self.__max_frequency_method(seqs, seq_type=seq_type, namespace=namespace)
        seq_type = frequency_dict['seq_type']
        frequency_df = frequency_dict['frequency_df']
        letter_df = None
        if type(seqs) == list:
            seq_count = len(seqs)
        else:
            seq_count = max(sum(seqs))
        if font is not None:
            font_df = get_font(font)
            letter_df = merge(font_df, frequency_df.copy(), on='letter')
            pad = stack_width / 2
            letter_df['x'] = new_range(letter_df['x'], letter_df['position'] - pad, letter_df['position'] + pad)
            letter_df['y'] = new_range(letter_df['y'], 1.5 - pad, 1.5 + pad)
            letter_df = letter_df[['x', 'y', 'letter', 'position', 'order']]
            letter_df['seq_group'] = seq_group
        frequency_df['x'] = frequency_df['position']
        frequency_df['y'] = frequency_df['frequency'] / seq_count / 2
        frequency_df['width'] = stack_width
        frequency_df['height'] = frequency_df['frequency']/ seq_count
        frequency_df['seq_group'] = seq_group
        return {'seq_type': seq_type, 'bar_data': frequency_df, 'letter_data': letter_df}

    def __max_frequency_method(self, seqs: Union[List[str], ndarray], seq_type: str, namespace: List[str]) -> Dict:
        max_frequency_dict = self.__make_max_frequency(seqs, seq_type, namespace)
        frequency_arr = max_frequency_dict['max_frequency_mat'][1].astype(float).tolist()
        letter_arr = max_frequency_dict['max_frequency_mat'][0].tolist()
        seq_type = max_frequency_dict['seq_type']
        frequency_df = DataFrame({
            'letter': letter_arr,
            'frequency': frequency_arr,
            'position': list(range(1, len(letter_arr) + 1))
        })
        return {'seq_type': seq_type, 'frequency_df': frequency_df}

    def __make_max_frequency(self, seqs: Union[List[str], ndarray], seq_type: str = 'AUTO',
                             namespace: List[str] = None) -> dict:
        def frequency_col(letter_col):
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
            return PFM_col

        def max_frequency_letter(col):
            max_freq = col[0]
            letter = namespace[0]
            for i in range(len(namespace)):
                if col[i] > max_freq:
                    max_freq = col[i]
                    letter = namespace[i]
            return array((letter, max_freq))

        if type(seqs) is ndarray:
            if seq_type == 'AUTO' and namespace is None:
                raise Exception("seq_type can not be 'AUTO', when namespace is None.")
            if seq_type != 'OTHER':
                namespace_dict = find_namespace(seq_type=seq_type)
                namespace = namespace_dict['namespace']
                seq_type = namespace_dict['seq_type']
            max_frequency_mat = apply_along_axis(max_frequency_letter, 0, seqs)
        else:
            letter_mat = letter_matrix(seqs)
            ns = find_namespace(letter_mat, seq_type, namespace=namespace)
            namespace = ns['namespace']
            seq_type = ns['seq_type']
            frequency_mat = apply_along_axis(frequency_col, 0, letter_mat)
            max_frequency_mat = apply_along_axis(max_frequency_letter, 0, frequency_mat)

        return {'seq_type': seq_type, 'max_frequency_mat': max_frequency_mat}

    def __radd__(self, gg):
        gg = gg + [self.bar_layer, self.letter_layer, self.scale_x_continuous, self.scale_y_continuous, self.ylab, self.xlab, self.colscale_opts]
        return gg
