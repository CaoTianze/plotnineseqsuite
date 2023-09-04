# Install plotnineSeqSuite: pip install plotnineseqsuite
# Install Pillow: pip install Pillow
from plotnine import ggplot, ggtitle

from plotnineseqsuite.data import seqs_dna, seqs_aa
from plotnineseqsuite.logo import geom_logo
from plotnineseqsuite.theme import theme_seq

A = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='chemistry') + ggtitle('A') + theme_seq()  # Fig. 2A
A.save('Fig. 2A.png')
B = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='chemistry2') + ggtitle('B') + theme_seq()  # Fig. 2B
B.save('Fig. 2B.png')
C = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='hydrophobicity') + ggtitle('C') + theme_seq()  # Fig. 2C
C.save('Fig. 2C.png')
D = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme='nucleotide') + ggtitle('D') + theme_seq()  # Fig. 2D
D.save('Fig. 2D.png')
E = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme='nucleotide2') + ggtitle('E') + theme_seq()  # Fig. 2E
E.save('Fig. 2E.png')
F = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme='base_pairing') + ggtitle('F') + theme_seq()  # Fig. 2F
F.save('Fig. 2F.png')
G = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='clustalx') + ggtitle('G') + theme_seq()  # Fig. 2G
G.save('Fig. 2G.png')
H = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='taylor') + ggtitle('H') + theme_seq()  # Fig. 2H
H.save('Fig. 2H.png')

from plotnine import ggplot
from plotnineseqsuite.data import seqs_dna
from plotnineseqsuite.col_schemes import make_col_scheme
from plotnineseqsuite.logo import geom_logo
from plotnineseqsuite.theme import theme_seq

cs1 = make_col_scheme(chars=['A', 'T', 'C', 'G'], groups=['gr1', 'gr1', 'gr2', 'gr2'],
                      cols=['purple', 'purple', 'blue', 'blue'])
I = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme=cs1) + ggtitle('I') + theme_seq()  # Fig. 2I
I.save('Fig. 2I.png')
cs2 = make_col_scheme(chars=['A', 'T', 'C', 'G'], values=[1, 2, 3, 4])
J = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme=cs2) + ggtitle('J') + theme_seq()  # Fig. 2J
J.save('Fig. 2J.png')

from plotnine import ggplot, coord_fixed, ggtitle, element_text
from plotnine.guides import guides
from plotnineseqsuite.data import seqs_dna
from plotnineseqsuite.logo import geom_logo
from plotnineseqsuite.theme import theme_seq
from plotnineseqsuite.align import geom_alignedSeq
from plotnineseqsuite.bar import geom_seqBar

seqs_numeric = list(
    map(lambda x: x.replace('A', 'a').replace('T', 't').replace('G', 'g').replace('C', 'c'), seqs_dna['MA0001.1']))
K = ggplot() + geom_logo(seqs_numeric, method='probability', namespace=['a', 't', 'g', 'c']) + ggtitle(
    'K') + theme_seq() + guides(fill=False)  # Fig .4K
K.save('Fig. 2K.png')
seqs_numeric = list(
    map(lambda x: x.replace('A', '1').replace('T', '2').replace('G', '3').replace('C', '4'), seqs_dna['MA0001.1']))
L = ggplot() + geom_logo(seqs_numeric, method='probability', namespace=['1', '2', '3', '4']) + ggtitle(
    'L') + theme_seq() + guides(fill=False)  # Fig .4L
L.save('Fig. 2L.png')
seqs_numeric = list(
    map(lambda x: x.replace('A', 'δ').replace('T', 'ε').replace('G', 'ψ').replace('C', 'λ'), seqs_dna['MA0001.1']))
M = ggplot() + geom_logo(seqs_numeric, method='probability', namespace=['δ', 'ε', 'ψ', 'λ']) + ggtitle(
    'M') + theme_seq() + guides(fill=False)  # Fig .4M
M.save('Fig. 2M.png')

import numpy as np

custom_mat = np.random.randn(4, 5)
N = ggplot() + geom_logo(custom_mat, method='custom', seq_type='DNA') + ggtitle('N') + theme_seq()# Fig .4N
N.save('Fig. 2N.png')
O = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font=None) + ggtitle('O') + theme_seq() + coord_fixed()  # Fig. 2O
O.save('Fig. 2O.png')
P = ggplot() + geom_seqBar(seqs_dna['MA0013.1'], font=None) + ggtitle('P') + theme_seq()# Fig. 2P
P.save('Fig. 2P.png')
Q = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], no_scheme_col='black', col_scheme=None) + ggtitle(
    'Q') + theme_seq() + coord_fixed()  # Fig. 2G
Q.save('Fig. 2Q.png')
from plotnine import scale_y_continuous

names = ['seq-a', 'seq-b', 'seq-c', 'seq-d', 'seq-e', 'seq-f']
seqs = geom_alignedSeq(seqs_dna['MA0013.1'], seq_names=names)
logo = geom_logo(seqs_dna['MA0013.1'], method='probability')
logo.data['y'] = logo.data['y'] + 6.1
bar = geom_seqBar(seqs_dna['MA0013.1'], font=None)
bar.bar_data['y'] = bar.bar_data['y'] - 1.1
R = ggplot() + logo + bar + seqs + ggtitle('R') + theme_seq()+ scale_y_continuous(
    breaks=lambda x: [k + 0.5 for k in range(0, len(names))], labels=names)  # Fig .4H
R.save('Fig. 2R.png')
from plotnine.geoms import annotate

S = ggplot() + geom_seqBar(seqs_dna['MA0013.1']) + annotate('segment', x=1.5, xend=2.5, y=0, yend=0, size=2,
                                                            color='red') + annotate('segment', x=4.5, xend=7.5, y=0,
                                                                                    yend=0, size=2,
                                                                                    color='red') + annotate('segment',
                                                                                                            x=8.5,
                                                                                                            xend=11.5,
                                                                                                            y=0, yend=0,
                                                                                                            size=2,
                                                                                                            color='red') + annotate(
    'text', x=6, y=-0.2, label='A is the most', color='red') + ggtitle('S') + theme_seq() # Fig .2I
S.save('Fig. 2S.png')

from PIL import Image

name2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
img2 = []
resize_img2 = []
for item in name2:
    img2.append(Image.open('Fig. 2%s.png' % item))
for item in img2:
    resize_img2.append(item.resize((img2[0].width, img2[0].height)))
coordinate2 = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1)
               , (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3)]
dst = Image.new('RGB', (img2[0].width * 5, img2[0].height * 4), color='white')
list(map(lambda img_item, coordinate_size: dst.paste(img_item, (
    img2[0].width * coordinate_size[0], img2[0].height * coordinate_size[1])), resize_img2, coordinate2))
dst.save('Fig. 2.png')

#Fig. 3
# name3 = ['A', 'B', 'C']
# img3 = []
# resize_img3 = []
# for item in name3:
#     img3.append(Image.open('compare/Fig. 3%s.png' % item))
# for item in img3:
#     resize_img3.append(item.resize((img3[0].width, img3[0].height)))
# coordinate3 = [(0, 0),(1,0),(2,0)]
# dst = Image.new('RGB', (img3[0].width * 3, img3[0].height * 1), color='white')
# list(map(lambda img_item, coordinate_size: dst.paste(img_item, (
#     img3[0].width * coordinate_size[0], img3[0].height * coordinate_size[1])), resize_img3, coordinate3))
# dst.save('Fig. 3.png')

#Fig. 4
from plotnine import ggplot, theme, guides, element_text, element_rect, element_blank, scale_fill_manual
from plotnineseqsuite import geom_logo

data = ['RELVKDRRWSPDSKKKIREGPSNGAHEERNWHPVDGANGVRRYVP', 'RELIKDRRWSPDSRNDIREGPSDGQHEERNWHPSNGANGVSRYIP',
        'RELIKDRRWSPDSRNNIREGPSDGQHEERNWHPSNGANGVSRYIP', 'RELIKDRRWSPDSRNNIREGPSDGQHEERNWHPSNGANGVSRYIP',
        'RELIKDRRWSPDSRNNIREGPSDGQHEERNWHPSNGANGVSRYIP', 'RELIKDRRWSPDSRNNIREGPSDGQHEERNWHPSNGANGVSRYIP',
        'RELIKDRRWSPDSRNNIREGPSDGQHEERNWHPSNGANGVSRYIP', 'RELIKDRRWSPDSRNNIREGPSDGQHEERNWHPSNGANGVSRYIP',
        'RELIKDRRWSPDSRNNIREGPSDGQHEERNWHPSNGANGVSRYIP', 'RELIKDRRWSPDSRNNIREGPSDGQHEERNWHPSNGANGVSRYIP']
g = ggplot() + geom_logo(data=data, method='probability')+ggtitle('A')
g = g + theme(aspect_ratio=0.1, panel_grid=element_blank(),
              panel_background=element_rect(fill='white'),
              axis_title_x=element_blank(), axis_text_x=element_blank(),
              axis_ticks_major_x=element_blank(), axis_ticks_major_y=element_blank(),
              axis_title_y=element_text(size=8)) + guides(fill=False)
g.save('Fig. 4A.png',dpi=300,width=6,height=1)

layer_logo = geom_logo(data=data, method='probability')


def change_group(x):
    if x['position'] == 1 or x['position'] == 6 or x['position'] == 19 or x['position'] == 29 or x['position'] == 42:
        x['group'] = 'interested'
    else:
        x['group'] = 'not_interested'
    return x


layer_logo.data = layer_logo.data.apply(func=change_group, axis=1)
g = ggplot() + layer_logo + ggtitle('B') + scale_fill_manual({'interested': '#B22222', 'not_interested': '#C0C0C0'})
g = g + theme(aspect_ratio=0.1, panel_grid=element_blank(), panel_background=element_rect(fill='white'),
              axis_title_x=element_blank(), axis_text_x=element_blank(), axis_ticks_major_x=element_blank(),
              axis_ticks_major_y=element_blank(), axis_title_y=element_text(size=8)) + guides(fill=False)
g.save('Fig. 4B.png', dpi=300,width=6,height=1)

name4 = ['A', 'B']
img4 = []
resize_img4 = []
for item in name4:
    img4.append(Image.open('Fig. 4%s.png' % item))
for item in img4:
    resize_img4.append(item.resize((img4[0].width, img4[0].height)))
coordinate4 = [(0, 0),(0,1)]
dst = Image.new('RGB', (img4[0].width * 1, img4[0].height * 2), color='white')
list(map(lambda img_item, coordinate_size: dst.paste(img_item, (
    img4[0].width * coordinate_size[0], img4[0].height * coordinate_size[1])), resize_img4, coordinate4))
dst.save('Fig. 4.png')