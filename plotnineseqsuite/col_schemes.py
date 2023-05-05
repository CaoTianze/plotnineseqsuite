from typing import List, Dict

from pandas import DataFrame

col_schemes = ['AUTO', 'chemistry', 'chemistry2', 'hydrophobicity', 'nucleotide', 'nucleotide2', 'base_pairing',
                   'clustalx', 'taylor']


def make_col_scheme(name:str='Custom Scheme', chars: List[str]=None, groups: List[int] = None, cols: List[int] = None, values: List[int] = None) -> Dict:
    if chars is None:
        raise Exception("'chars' can't be None")
    if values is None:
        if len(chars) != len(cols):
            raise Exception('"chars" and "cols" must have same length')
        if groups is None:
            groups = chars
        data = {
            'letter': chars,
            'group': groups,
            'col': cols
        }
        cs = DataFrame(data=data)
    else:
        if len(chars) != len(values):
            raise Exception('"chars" and "values" must have same length')
        data = {
            'letter': chars,
            'group': values
        }
        cs = DataFrame(data=data)
    return {'name':name, 'cs':cs}


def get_col_scheme(col_scheme: str, seq_type: str = 'AUTO') -> Dict:
    if col_scheme == 'AUTO':
        if seq_type == 'AUTO':
            raise Exception('"col_scheme" and "seq_type" cannot both be "AUTO"')
        if seq_type == 'AA':
            col_scheme = 'chemistry'
        elif seq_type == 'DNA':
            col_scheme = 'nucleotide'
        elif seq_type == 'RNA':
            col_scheme = 'nucleotide'
        else:
            col_scheme = 'nucleotide'
    if col_scheme == 'chemistry2':
        cs = DataFrame(data={
            'letter': ['G', 'S', 'T', 'Y', 'C', 'N', 'Q', 'K', 'R', 'H', 'D', 'E', 'P', 'A', 'W', 'F', 'L', 'I', 'M',
                       'V'],
            'group': ['Polar', 'Polar', 'Polar', 'Polar', 'Polar', 'Neutral', 'Neutral', 'Basic', 'Basic', 'Basic',
                      'Acidic', 'Acidic', 'Hydrophobic', 'Hydrophobic', 'Hydrophobic', 'Hydrophobic', 'Hydrophobic',
                      'Hydrophobic', 'Hydrophobic', 'Hydrophobic'],
            'col': ['#058644', '#058644', '#058644', '#058644', '#058644', '#720091', '#720091', '#0046C5', '#0046C5',
                    '#0046C5', '#C5003E', '#C5003E', '#2E2E2E', '#2E2E2E', '#2E2E2E', '#2E2E2E', '#2E2E2E', '#2E2E2E',
                    '#2E2E2E', '#2E2E2E']
        })
    elif col_scheme == 'chemistry':
        cs = DataFrame(data={
            'letter': ['G', 'S', 'T', 'Y', 'C', 'N', 'Q', 'K', 'R', 'H', 'D', 'E', 'P', 'A', 'W', 'F', 'L', 'I', 'M',
                       'V'],
            'group': ['Polar', 'Polar', 'Polar', 'Polar', 'Polar', 'Neutral', 'Neutral', 'Basic', 'Basic', 'Basic',
                      'Acidic', 'Acidic', 'Hydrophobic', 'Hydrophobic', 'Hydrophobic', 'Hydrophobic', 'Hydrophobic',
                      'Hydrophobic', 'Hydrophobic', 'Hydrophobic'],
            'col': ['#109648', '#109648', '#109648', '#109648', '#109648', '#5E239D', '#5E239D', '#255C99', '#255C99',
                    '#255C99', '#D62839', '#D62839', '#221E22', '#221E22', '#221E22', '#221E22', '#221E22', '#221E22',
                    '#221E22', '#221E22']
        })
    elif col_scheme == 'hydrophobicity':
        cs = DataFrame(data={
            'letter': ['I', 'V', 'L', 'F', 'C', 'M', 'A', 'G', 'T', 'W', 'S', 'Y', 'P', 'H', 'D', 'E', 'N', 'Q', 'K',
                       'R'],
            'group': [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.9, -0.8, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5,
                      -3.5, -3.9, -4.5]})
    elif col_scheme == 'nucleotide2':
        cs = DataFrame(data={
            'letter': ['A', 'C', 'G', 'T', 'U'],
            'col': ['darkgreen', 'blue', 'orange', 'red', 'red']
        })
    elif col_scheme == 'nucleotide':
        cs = DataFrame(data={
            'letter': ['A', 'C', 'G', 'T', 'U'],
            'col': ['#109648', '#255C99', '#F7B32B', '#D62839', '#D62839']
        })
    elif col_scheme == 'base_pairing':
        cs = DataFrame(data={
            'letter': ['A', 'T', 'U', 'G', 'C'],
            'group': ['Weak bonds', 'Weak bonds', 'Weak bonds', 'Strong bonds', 'Strong bonds', ],
            'col': ['darkorange', 'darkorange', 'darkorange', 'blue', 'blue']
        })
    elif col_scheme == 'clustalx':
        cs = DataFrame(data={
            'letter': ['W', 'L', 'V', 'I', 'M', 'F', 'A', 'R', 'K', 'T', 'S', 'N', 'Q', 'D', 'E', 'H', 'Y', 'C', 'G',
                       'P'],
            'col': ['#197FE5', '#197FE5', '#197FE5', '#197FE5', '#197FE5', '#197FE5', '#197FE5', '#E53319', '#E53319',
                    '#19CC19', '#19CC19', '#19CC19', '#19CC19', '#CC4CCC', '#CC4CCC', '#19B2B2', '#19B2B2', '#E57F7F',
                    '#E5994C', '#B0B000']
        })
    elif col_scheme == 'taylor':
        cs = DataFrame(data={
            'letter': ['D', 'S', 'T', 'G', 'P', 'C', 'A', 'V', 'I', 'L', 'M', 'F', 'Y', 'W', 'H', 'R', 'K', 'N', 'Q',
                       'E'],
            'col': ['#FF0000', '#FF3300', '#FF6600', '#FF9900', '#FFCC00', '#FFFF00', '#CCFF00', '#99FF00', '#66FF00',
                    '#33FF00', '#00FF00', '#00FF66', '#00FFCC', '#00CCFF', '#0066FF', '#0000FF', '#6600FF', '#CC00FF',
                    '#FF00CC', '#FF0066']
        })
    if 'group' not in cs.columns:
        cs['group'] = cs['letter']

    return {'name':col_scheme,
        'cs':cs}
