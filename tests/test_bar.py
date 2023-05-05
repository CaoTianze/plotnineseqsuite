from numpy import array
from plotnine import ggplot

from plotnineseqsuite.bar import geom_seqBar
from plotnineseqsuite.theme import theme_seq


def test_make_max_frequency():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    a=geom_seqBar(seqs)._geom_seqbar__make_max_frequency(seqs)
    assert (a['max_frequency_mat'][0] == array(['T','A','G','T','A','A','A','C','A','A','A'])).all()

def test_max_frequency_method():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    a = geom_seqBar(seqs)._geom_seqbar__max_frequency_method(seqs, seq_type='AUTO', namespace=None)
    assert a['frequency_df'].size == 11*3

def test_geom_seqBar():
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    ggplot() + geom_seqBar(seqs) + theme_seq()
    ggplot() + geom_seqBar(seqs, font=None) + theme_seq()
