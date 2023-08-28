from plotnineseqsuite.tool import extract, arrange
from plotnine import ggplot, ggtitle

from plotnineseqsuite.data import seqs_aa
from plotnineseqsuite.logo import geom_logo
from plotnineseqsuite.theme import theme_seq


def test_extract():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    result = extract(seqs, start=1, end=4)


def test_arrange():
    A = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='chemistry') + ggtitle('A') + theme_seq()
    B = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='chemistry2') + ggtitle('B') + theme_seq()
    arrange(A, B)
    arrange(A, B, 'vertical')
    arrange(A, B, filename ='xx.pdf')
    arrange(A, B, filename ='xx.png')
    