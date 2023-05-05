from plotnine import ggplot, facet_wrap

from plotnineseqsuite.align import geom_alignedSeq
from plotnineseqsuite.theme import theme_seq
from plotnineseqsuite.data import seqs_dna

def test_geom_alignedSeq():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA',
            'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    ggplot() + geom_alignedSeq(data=seqs, font=None) + theme_seq()
    ggplot() + geom_alignedSeq(data=seqs_dna['MA0013.1'], font=None) + theme_seq()
    ggplot() + geom_alignedSeq(data=seqs) + theme_seq()
    ggplot() + geom_alignedSeq(data=seqs_dna['MA0013.1']) + theme_seq()
    ggplot() + geom_alignedSeq(data=seqs,
                               seq_names=['test-aaa', 'test-b', 'test-c', 'test-d', 'test-e', 'test-ff']) + theme_seq()
    ggplot() + geom_alignedSeq(data=seqs, font_col='black', bg_col_scheme=None) + theme_seq()
