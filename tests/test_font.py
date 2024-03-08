import pytest
from pandas import DataFrame
from plotnine import ggplot, ggtitle

import plotnineseqsuite.font as pf
import plotnine.options as op

from plotnineseqsuite import geom_logo, theme_seq
from plotnineseqsuite.data import seqs_dna


def test_import_font():
    assert type(pf.xkcd_regular) == DataFrame


def test_get_fonts():
    assert type(pf.get_font('akrobat_bold')) == DataFrame
    with pytest.raises(Exception):
        pf.get_font('1')


def test_list_fonts():
    assert len( pf.list_fonts() ) == 15

def test_font_draw():
    op.figure_size = (5.7,2.9)
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    ggplot() + geom_logo(data=seqs, font='xkcd_regular') + theme_seq()+ggtitle('xkcd_regular')
    fonts = pf.list_fonts()
    for i in range(0, 15, 3):
        print(ggplot() + geom_logo(data=seqs_dna['MA0001.1'], font=fonts[i]) + theme_seq() + ggtitle(fonts[i]))
        print(ggplot() + geom_logo(data=seqs_dna['MA0001.1'], font=fonts[i + 1]) + theme_seq() + ggtitle(fonts[i + 1]))
        print(ggplot() + geom_logo(data=seqs_dna['MA0001.1'], font=fonts[i + 2]) + theme_seq() + ggtitle(fonts[i + 2]))
