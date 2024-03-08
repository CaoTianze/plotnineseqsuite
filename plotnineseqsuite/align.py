from functools import reduce
from math import floor, ceil
from typing import List, Dict, Union

from pandas import merge, DataFrame, concat
from pandas.core.dtypes.common import is_numeric_dtype
from plotnine import scale_fill_gradient, scale_fill_manual, aes, geom_tile, \
    scale_x_continuous, geom_polygon, xlab, ylab, scale_y_continuous

from plotnineseqsuite.col_schemes import get_col_scheme
from plotnineseqsuite.common import find_namespace, letter_matrix, new_range
from plotnineseqsuite.font import get_font


class geom_alignedSeq:

    def __init__(self, data: Union[List[str], Dict] = None, seq_names: List[str] = None, seq_type: str = 'AUTO',
                 namespace: List[str] = None,
                 font: str = 'roboto_medium', stack_width: float = 0.75, border_col: str = 'grey',
                 scheme_applied: str = 'BACKGROUND', no_scheme_col: str = '#000000',
                 col_scheme: Union[Dict, str] = 'AUTO',
                 low_col: str = 'black', high_col: str = 'yellow', na_col: str = '#333333',
                 **kwargs):
        self.__kwargs = kwargs
        self.__no_scheme_col = no_scheme_col
        self.__border_col = border_col
        self.__scheme_applied = scheme_applied
        if stack_width > 1 or stack_width <= 0:
            raise Exception('"stack_width" must be between 0 and 1')
        if data is None:
            raise Exception('Missing "data" parameter!')
        if namespace is not None:
            seq_type = 'OTHER'
        if seq_type not in {'OTHER', 'AUTO', 'AA', 'DNA', 'RNA'}:
            raise Exception("seq_type must be one of 'OTHER' or 'AUTO', or 'AA', or 'DNA', or 'RNA'")
        if scheme_applied not in {'BACKGROUND', 'LETTER'}:
            raise Exception("scheme_applied must be one of 'BACKGROUND' or 'LETTER'")
        if type(data) == list:
            data = {1: data}
        lvls = data.keys()
        data_sp = list(map(lambda x: self.__aligned_data(data[x], stack_width=stack_width,
                                                         seq_group=x,
                                                         seq_type=seq_type,
                                                         font=font, namespace=namespace), lvls))
        seq_type = data_sp[0]['seq_type']
        bg_data = reduce(lambda x, y: concat([x, y]), map(lambda x: x['bg_data'], data_sp))
        if font is not None:
            letter_data = reduce(lambda x, y: concat([x, y]), map(lambda x: x['letter_data'], data_sp))

        if type(col_scheme) is str:
            cs_dict = get_col_scheme(col_scheme, seq_type)
        elif type(col_scheme) is dict and type(col_scheme['cs']) == DataFrame:
            cs_dict = col_scheme

        if col_scheme is not None:
            legend_title = cs_dict['name']
            colscale_gradient = True if is_numeric_dtype(cs_dict['cs']['group']) else False
            if colscale_gradient:
                if not any(cs_dict['cs']['letter'].isin(['-'])):
                    cs_dict['cs'] = concat([cs_dict['cs'], DataFrame(data={'letter': ['-'], 'group': [0]})])
                colscale_opts = scale_fill_gradient(low=low_col, high=high_col, name=legend_title,
                                                    na_value=na_col)
            else:
                if not any(cs_dict['cs']['letter'].isin(['-'])):
                    cs_dict['cs'] = concat(
                        [cs_dict['cs'], DataFrame(data={'letter': ['-'], 'group': ['-'], 'col': ['#FFFFFF']})])
                tmp = cs_dict['cs'].drop_duplicates(subset=['group']).dropna(subset=['group'])
                col_map = {}
                for item in map(lambda x, y: {x: y}, tmp['group'], tmp['col']):
                    col_map.update(item)
                colscale_opts = scale_fill_manual(values=col_map, name=legend_title, na_value=na_col)
            if scheme_applied == 'BACKGROUND':
                bg_data = merge(bg_data, cs_dict['cs'], how='left')
            else:
                letter_data = merge(letter_data, cs_dict['cs'], how='left')
            self.colscale_opts = colscale_opts
        else:
            if scheme_applied == 'BACKGROUND':
                bg_data = None
            else:
                letter_data = None
            self.colscale_opts = None

        if font is not None:
            letter_data = letter_data.sort_values(by='order').reset_index(drop=True)
            letter_data['group_by'] = letter_data.apply(
                lambda x: '{}.{}.{}.{}'.format(x['seq_group'], x['letter'], x['position'], x['y_index']), axis=1)
        else:
            letter_data = None
        self.bg_data = bg_data
        self.letter_data = letter_data
        self.scale_x_continuous = scale_x_continuous(breaks=lambda x: range(floor(x[0]), ceil(x[1])), expand=(0, 0))
        self.scale_y_continuous = scale_y_continuous(breaks=None)
        if seq_names is not None:
            self.scale_y_continuous = scale_y_continuous(breaks=lambda x: [k + 0.5 for k in range(0, int(x[1]))],
                                                         labels=seq_names)
        self.ylab = ylab('Consensus')
        self.xlab = xlab('')

    def __aligned_data(self, seqs, font, stack_width=0.95, seq_group=1,
                       seq_type='AUTO', namespace=None):
        positioned_letter_dict = self.__positioned_letter_method(seqs, seq_type=seq_type, namespace=namespace)
        seq_type = positioned_letter_dict['seq_type']
        bg_df = positioned_letter_dict['bg_df']
        letter_df = None
        if font is not None:
            font_df = get_font(font)
            letter_df = merge(font_df, bg_df.copy(), on='letter')
            pad = stack_width / 2
            letter_df['x'] = new_range(letter_df['x'], letter_df['position'] - pad, letter_df['position'] + pad)
            letter_df['y'] = new_range(letter_df['y'], letter_df['y_index'] + 0.5 - pad,
                                       letter_df['y_index'] + 0.5 + pad)
            letter_df = letter_df[['x', 'y', 'letter', 'position', 'y_index', 'order']]
            letter_df['seq_group'] = seq_group
        bg_df['x'] = bg_df['position']
        bg_df['y'] = bg_df['y_index'] + 0.5
        bg_df['width'] = 1
        bg_df['height'] = 1
        bg_df['seq_group'] = seq_group
        return {'seq_type': seq_type, 'bg_data': bg_df, 'letter_data': letter_df}

    def __positioned_letter_method(self, seqs: List[str], seq_type: str, namespace: List[str]) -> Dict:
        positioned_letter_dict = self.__make_positioned_letter(seqs, seq_type, namespace)
        positioned_letter_arr = positioned_letter_dict['positioned_letter_arr']
        seq_type = positioned_letter_dict['seq_type']
        bg_df = DataFrame(columns=['letter', 'position', 'y_index'],
                          data=positioned_letter_arr)
        return {'seq_type': seq_type, 'bg_df': bg_df}

    def __make_positioned_letter(self, seqs: List[str], seq_type: str = 'AUTO',
                                 namespace: List[str] = None) -> dict:
        def to_df_data(x, y_index):
            x = list(x)
            l = len(x)
            return list(map(lambda letter, index: [letter, index + 1, y_index], x, range(l)))

        letter_mat = letter_matrix(seqs)
        ns = find_namespace(letter_mat, seq_type, namespace=namespace)
        seq_type = ns['seq_type']
        positioned_letter_arr = reduce(lambda x, y: x + y, map(lambda x, y: to_df_data(x, y), seqs, range(len(seqs))))
        return {'seq_type': seq_type, 'positioned_letter_arr': positioned_letter_arr}

    def __radd__(self, gg):
        params = []
        if self.bg_data is not None:
            if self.__scheme_applied == 'BACKGROUND':
                bg_layer = geom_tile(data=self.bg_data,
                                     mapping=aes(x='x', y='y', width='width', height='height', fill='group'),
                                     color=self.__border_col,
                                     **self.__kwargs)
            else:
                bg_layer = geom_tile(data=self.bg_data,
                                     mapping=aes(x='x', y='y', width='width', height='height'),
                                     fill=self.__no_scheme_col,
                                     color=self.__border_col,
                                     **self.__kwargs)
            params.append(bg_layer)
            params.append(self.colscale_opts)
        if self.letter_data is not None:
            if self.__scheme_applied == 'BACKGROUND':
                letter_layer = geom_polygon(data=self.letter_data, mapping=aes(x='x', y='y', group='group_by'),
                                            fill=self.__no_scheme_col, **self.__kwargs)
            else:
                letter_layer = geom_polygon(data=self.letter_data,
                                            mapping=aes(x='x', y='y', group='group_by', fill='group'),
                                            **self.__kwargs)
            params.append(letter_layer)
        params.extend([self.scale_x_continuous, self.scale_y_continuous, self.ylab, self.xlab])
        for param in params:
            gg += param
        return gg
