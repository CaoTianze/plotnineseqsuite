import pytest
from pandas import DataFrame
from plotnine import ggplot, ggtitle
import patchworklib as pw

import plotnineseqsuite.font as pf
import plotnine.options as op

def test_import_font():
    assert type(pf.xkcd_regular) == DataFrame


def test_get_fonts():
    assert type(pf.get_font('akrobat_bold')) == DataFrame
    with pytest.raises(Exception):
        pf.get_font('1')


def test_list_fonts():
    assert len( pf.list_fonts() ) == 12

def test_font_draw():
    op.figure_size = (5.7,2.9)
    seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
    ggplot() + geom_logo(data=seqs, font='xkcd_regular') + theme_logo()+ggtitle('xkcd_regular')
    fonts = pf.list_fonts()
    for i in range(0,12,3):
        g1 = pw.load_ggplot(ggplot() + geom_logo(data=seqs, font=fonts[i]) + theme_logo()+ggtitle(fonts[i]))
        g2 = pw.load_ggplot(ggplot() + geom_logo(data=seqs, font=fonts[i+1]) + theme_logo() + ggtitle(fonts[i+1]))
        g3 = pw.load_ggplot(ggplot() + geom_logo(data=seqs, font=fonts[i+2]) + theme_logo() + ggtitle(fonts[i+2]))
        if i == 0:
            allgg = g1|g2|g3
        else:
            temp = g1|g2|g3
            allgg = temp/allgg

    allgg.savefig()
