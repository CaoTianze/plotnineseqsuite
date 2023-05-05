from plotnine import ggplot

from plotnineseqsuite.col_schemes import *
from plotnineseqsuite.logo import geom_logo

def test_make_col_scheme():
    cs1 = make_col_scheme(chars=['A', 'T', 'G', 'C'], groups=['g1', 'g1', 'g2', 'g2'],
                          cols=['red', 'red', 'blue', 'blue'])
    cs2 = make_col_scheme(chars=['A', 'T', 'G', 'C'], cols=['red', 'red', 'blue', 'blue'])
    cs3 = make_col_scheme(chars=['A', 'T', 'G', 'C'], values=[1, 2, 3, 4])
    assert cs1['cs'].size == 4 * 3
    assert cs2['cs'].size == 4 * 3
    assert cs3['cs'].size == 4 * 2
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    #ggplot()+geom_logo(data=seqs,col_scheme='base_pairing')+theme_logo()
    cs1 = make_col_scheme(chars=['A', 'T', 'C', 'G'], groups=['gr1', 'gr1', 'gr2', 'gr2'],
                          cols=['purple', 'purple', 'blue', 'blue'])
    #ggplot() + geom_logo(data=seqs, col_scheme=cs1) + theme_logo()
    cs2 = make_col_scheme(chars=['A', 'T', 'C', 'G'], values=[1,2,3,4])
    #ggplot() + geom_logo(data=seqs, col_scheme=cs2) + theme_logo()


def test_get_col_scheme():
    cs1 = get_col_scheme(col_scheme='AUTO',seq_type='rna')
    cs2 = get_col_scheme(col_scheme='taylor')
    assert cs1['cs'].size == 5*3
    assert cs1['name'] == 'nucleotide'
    assert cs2['cs'].size == 20*3