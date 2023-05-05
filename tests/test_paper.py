# In order to execute the code correctly, the user needs to ensure that there is a 'paper' directory in the working directory.
# Install plotnineSeqSuite: pip install plotnineseqsuite
# Install Pillow: pip install Pillow
from plotnine import ggplot, ggtitle, theme, element_text

from plotnineseqsuite.data import seqs_dna, seqs_aa
from plotnineseqsuite.logo import geom_logo
from plotnineseqsuite.theme import theme_seq

A = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='chemistry') + ggtitle('A') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2A
A.save('paper/Fig. 2A.png')
B = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='chemistry2') + ggtitle('B') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2B
B.save('paper/Fig. 2B.png')
C = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='hydrophobicity') + ggtitle('C') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2C
C.save('paper/Fig. 2C.png')
D = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme='nucleotide') + ggtitle('D') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2D
D.save('paper/Fig. 2D.png')
E = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme='nucleotide2') + ggtitle('E') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2E
E.save('paper/Fig. 2E.png')
F = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme='base_pairing') + ggtitle('F') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2F
F.save('paper/Fig. 2F.png')
G = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='clustalx') + ggtitle('G') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2G
G.save('paper/Fig. 2G.png')
H = ggplot() + geom_logo(seqs_aa['CSNK2A2'], col_scheme='taylor') + ggtitle('H') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2H
H.save('paper/Fig. 2H.png')
from plotnine import ggplot
from plotnineseqsuite.data import seqs_dna
from plotnineseqsuite.col_schemes import make_col_scheme
from plotnineseqsuite.logo import geom_logo
from plotnineseqsuite.theme import theme_seq

cs1 = make_col_scheme(chars=['A', 'T', 'C', 'G'], groups=['gr1', 'gr1', 'gr2', 'gr2'],
                      cols=['purple', 'purple', 'blue', 'blue'])
I = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme=cs1) + ggtitle('I') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2I
I.save('paper/Fig. 2I.png')
cs2 = make_col_scheme(chars=['A', 'T', 'C', 'G'], values=[1, 2, 3, 4])
J = ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme=cs2) + ggtitle('J') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 2J
J.save('paper/Fig. 2J.png')

from plotnine import ggplot, coord_fixed, ggtitle, theme, element_text
from plotnineseqsuite.align import geom_alignedSeq
from plotnineseqsuite.theme import theme_seq
from plotnineseqsuite.data import seqs_dna

A = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='times_new_roman') + ggtitle('A') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3A
A.save('paper/Fig. 3A.png')
B = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='arial') + ggtitle('B') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3A
B.save('paper/Fig. 3B.png')
C = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='courier_new') + ggtitle('C') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3A
C.save('paper/Fig. 3C.png')
D = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='xkcd_regular') + ggtitle('D') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3A
D.save('paper/Fig. 3D.png')
E = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='akrobat_bold') + ggtitle('E') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3B
E.save('paper/Fig. 3E.png')
F = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='akrobat_regular') + ggtitle('F') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3C
F.save('paper/Fig. 3F.png')
G = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='helvetica_bold') + ggtitle('G') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3D
G.save('paper/Fig. 3G.png')
H = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='helvetica_light') + ggtitle('H') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3E
H.save('paper/Fig. 3H.png')
I = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='helvetica_regular') + ggtitle('I') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3F
I.save('paper/Fig. 3I.png')

J = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='roboto_bold') + ggtitle('J') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3G
J.save('paper/Fig. 3J.png')
K = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='roboto_medium') + ggtitle('K') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3H
K.save('paper/Fig. 3K.png')
L = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='roboto_regular') + ggtitle('L') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3I
L.save('paper/Fig. 3L.png')

M = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='roboto_slab_bold') + ggtitle('M') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3J
M.save('paper/Fig. 3M.png')
N = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='roboto_slab_light') + ggtitle('N') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3K
N.save('paper/Fig. 3N.png')
O = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font='roboto_slab_regular') + ggtitle('O') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig .3L
O.save('paper/Fig. 3O.png')

from plotnine import ggplot, coord_fixed, ggtitle, theme, element_text
from plotnine.guides import guides
from plotnineseqsuite.data import seqs_dna
from plotnineseqsuite.logo import geom_logo
from plotnineseqsuite.theme import theme_seq
from plotnineseqsuite.align import geom_alignedSeq
from plotnineseqsuite.bar import geom_seqBar

seqs_numeric = list(
    map(lambda x: x.replace('A', 'a').replace('T', 't').replace('G', 'g').replace('C', 'c'), seqs_dna['MA0001.1']))
A = ggplot() + geom_logo(seqs_numeric, method='probability', namespace=['a', 't', 'g', 'c']) + ggtitle(
    'A') + theme_seq() + theme(plot_title=element_text(size=30, ha='left')) + guides(fill=False)  # Fig .4A
A.save('paper/Fig. 4A.png')
seqs_numeric = list(
    map(lambda x: x.replace('A', '1').replace('T', '2').replace('G', '3').replace('C', '4'), seqs_dna['MA0001.1']))
B = ggplot() + geom_logo(seqs_numeric, method='probability', namespace=['1', '2', '3', '4']) + ggtitle(
    'B') + theme_seq() + theme(plot_title=element_text(size=30, ha='left')) + guides(fill=False)  # Fig .4B
B.save('paper/Fig. 4B.png')
seqs_numeric = list(
    map(lambda x: x.replace('A', 'δ').replace('T', 'ε').replace('G', 'ψ').replace('C', 'λ'), seqs_dna['MA0001.1']))
C = ggplot() + geom_logo(seqs_numeric, method='probability', namespace=['δ', 'ε', 'ψ', 'λ']) + ggtitle(
    'C') + theme_seq() + theme(plot_title=element_text(size=30, ha='left')) + guides(fill=False)  # Fig .4C
C.save('paper/Fig. 4C.png')
import numpy as np

custom_mat = np.random.randn(4, 5)
D = ggplot() + geom_logo(custom_mat, method='custom', seq_type='DNA') + ggtitle('D') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig .4D
D.save('paper/Fig. 4D.png')
E = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font=None) + ggtitle('E') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig. 4E
E.save('paper/Fig. 4E.png')
F = ggplot() + geom_seqBar(seqs_dna['MA0013.1'], font=None) + ggtitle('F') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig. 4F
F.save('paper/Fig. 4F.png')
G = ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font_col='black', bg_col_scheme=None) + ggtitle(
    'G') + theme_seq() + theme(plot_title=element_text(size=30, ha='left')) + coord_fixed()  # Fig. 4G
G.save('paper/Fig. 4G.png')
from plotnine import scale_y_continuous

names = ['seq-a', 'seq-b', 'seq-c', 'seq-d', 'seq-e', 'seq-f']
seqs = geom_alignedSeq(seqs_dna['MA0013.1'], seq_names=names)
logo = geom_logo(seqs_dna['MA0013.1'], method='probability')
logo.data['y'] = logo.data['y'] + 6.1
bar = geom_seqBar(seqs_dna['MA0013.1'], font=None)
bar.bar_data['y'] = bar.bar_data['y'] - 1.1
H = ggplot() + logo + bar + seqs + ggtitle('H') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left')) + scale_y_continuous(
    breaks=lambda x: [k + 0.5 for k in range(0, len(names))], labels=names)  # Fig .4H
H.save('paper/Fig. 4H.png')
from plotnine.geoms import annotate

I = ggplot() + geom_seqBar(seqs_dna['MA0013.1']) + annotate('segment', x=1.5, xend=2.5, y=0, yend=0, size=2,
                                                            color='red') + annotate('segment', x=4.5, xend=7.5, y=0,
                                                                                    yend=0, size=2,
                                                                                    color='red') + annotate('segment',
                                                                                                            x=8.5,
                                                                                                            xend=11.5,
                                                                                                            y=0, yend=0,
                                                                                                            size=2,
                                                                                                            color='red') + annotate(
    'text', x=6, y=-0.2, label='A is the most', color='red') + ggtitle('I') + theme_seq() + theme(
    plot_title=element_text(size=30, ha='left'))  # Fig .4I
I.save('paper/Fig. 4I.png')

from PIL import Image

name2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
img2 = []
resize_img2=[]
for item in name2:
    img2.append(Image.open('paper/Fig. 2%s.png' % item))
for item in img2:
    resize_img2.append(item.resize((img2[0].width,img2[0].height)))
coordinate2 = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
dst = Image.new('RGB', (img2[0].width * 5, img2[0].height * 2))
list(map(lambda img_item, coordinate_size: dst.paste(img_item, (
img2[0].width * coordinate_size[0], img2[0].height * coordinate_size[1])), resize_img2, coordinate2))
dst.save('paper/Fig. 2.png')

name3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O']
img3 = []
resize_img3=[]
for item in name3:
    img3.append(Image.open('paper/Fig. 3%s.png' % item))
for item in img3:
    resize_img3.append(item.resize((img3[0].width,img3[0].height)))
coordinate3 = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2), (0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4)]
dst = Image.new('RGB', (img3[0].width * 3, img3[0].height * 5))
list(map(lambda img_item, coordinate_size: dst.paste(img_item, (
img3[0].width * coordinate_size[0], img3[0].height * coordinate_size[1])), resize_img3, coordinate3))
dst.save('paper/Fig. 3.png')

name4 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
img4 = []
resize_img4=[]
for item in name4:
    img4.append(Image.open('paper/Fig. 4%s.png' % item))
for item in img4:
    resize_img4.append(item.resize((img4[0].width,img4[0].height)))
coordinate4 = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
dst = Image.new('RGB', (img4[0].width * 3, img4[0].height * 3))
list(map(lambda img_item, coordinate_size: dst.paste(img_item, (
img4[0].width * coordinate_size[0], img4[0].height * coordinate_size[1])), resize_img4, coordinate4))
dst.save('paper/Fig. 4.png')