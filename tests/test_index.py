import numpy as np
from plotnine import ggplot, facet_wrap, ggtitle, coord_fixed, scale_y_continuous
from plotnine.geoms import annotate
from plotnine.guides import guides
from plotnineseqsuite.align import geom_alignedSeq
from plotnineseqsuite.bar import geom_seqBar
from plotnineseqsuite.col_schemes import make_col_scheme
from plotnineseqsuite.data import seqs_dna, seqs_aa, pfms_dna
from plotnineseqsuite.font import list_fonts
from plotnineseqsuite.logo import geom_logo
from plotnineseqsuite.theme import theme_seq


#test_plot_an_aligned_sequences():
ggplot() + geom_alignedSeq(seqs_dna['MA0013.1']) + theme_seq() + coord_fixed()


#test_no_background_color():
ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], no_scheme_col='black', col_scheme=None) + theme_seq() + coord_fixed()


#test_no_sequence_letter():
ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], font=None, border_col=None) + theme_seq() + coord_fixed()


#test_switch_color_schme():
ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], no_scheme_col='white', scheme_applied='LETTER') + theme_seq() + coord_fixed()


#test_tagging_sequences():
names = ['seq-a', 'seq-b', 'seq-c', 'seq-d', 'seq-e', 'seq-f']
ggplot() + geom_alignedSeq(seqs_dna['MA0013.1'], seq_names=names) + theme_seq() + coord_fixed()


#test_plot_a_sequence_logo():
ggplot() + geom_logo(seqs_dna['MA0001.1']) + theme_seq()


#test_accepted_input_formats():
ggplot() + geom_logo(pfms_dna['MA0018.2'], seq_type='DNA') + theme_seq()


#test_plotting_methods():
ggplot() + geom_logo(seqs_dna['MA0001.1'], method='bits') + theme_seq()
ggplot() + geom_logo(seqs_dna['MA0001.1'], method='probability') + theme_seq()


#test_custom_height_logos():
custom_mat = np.random.randn(4, 5)
ggplot() + geom_logo(custom_mat, method='custom', seq_type='DNA') + theme_seq()


#test_plot_a_sequence_bar():
ggplot() + geom_seqBar(seqs_dna['MA0013.1']) + theme_seq()


#test_bar_accepted_input_formats():
ggplot() + geom_seqBar(pfms_dna['MA0018.2'], seq_type='DNA') + theme_seq()


#test_bar_no_sequence_letter():
ggplot() + geom_seqBar(seqs_dna['MA0013.1'], font=None) + theme_seq()


#test_preset_alphabets():
ggplot() + geom_logo(seqs_aa['AKT1'], seq_type='AA') + theme_seq()


#test_custom_alphabet():
seqs_numeric = list(
    map(lambda x: x.replace('A', '1').replace('T', '2').replace('G', '3').replace('C', '4'), seqs_dna['MA0001.1']))
ggplot() + geom_logo(seqs_numeric, method='probability', namespace=['1', '2', '3', '4']) + theme_seq()+guides(fill=False)
seqs_numeric = list(
    map(lambda x: x.replace('A', 'δ').replace('T', 'ε').replace('G', 'ψ').replace('C', 'λ'), seqs_dna['MA0001.1']))
ggplot() + geom_logo(seqs_numeric, method='probability', namespace=['δ', 'ε', 'ψ', 'λ']) + theme_seq()+guides(fill=False)


#test_preset_color_schemes():
ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme='base_pairing') + theme_seq()


#test_custom_color_schemes():
cs1 = make_col_scheme(chars=['A', 'T', 'C', 'G'], groups=['gr1', 'gr1', 'gr2', 'gr2'],
                      cols=['purple', 'purple', 'blue', 'blue'])
ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme=cs1) + theme_seq()
cs2 = make_col_scheme(chars=['A', 'T', 'C', 'G'], values=[1, 2, 3, 4])
ggplot() + geom_logo(seqs_dna['MA0001.1'], col_scheme=cs2) + theme_seq()


#test_multiple_grouped_sequences():
ggplot() + geom_logo(seqs_dna) + theme_seq() + facet_wrap('~seq_group', ncol=4, scales='free_x')


#test_fonts():
fonts = list_fonts()
for i in range(0, 15, 3):
    print(ggplot() + geom_logo(data=seqs_dna['MA0001.1'], font=fonts[i]) + theme_seq() + ggtitle(fonts[i]))
    print(ggplot() + geom_logo(data=seqs_dna['MA0001.1'], font=fonts[i + 1]) + theme_seq() + ggtitle(fonts[i + 1]))
    print(ggplot() + geom_logo(data=seqs_dna['MA0001.1'], font=fonts[i + 2]) + theme_seq() + ggtitle(fonts[i + 2]))


#test_combining_plots():
names = ['seq-a', 'seq-b', 'seq-c', 'seq-d', 'seq-e', 'seq-f']
seqs = geom_alignedSeq(seqs_dna['MA0013.1'], seq_names=names)
logo = geom_logo(seqs_dna['MA0013.1'], method='probability')
logo.data['y'] = logo.data['y'] + 6.1
bar = geom_seqBar(seqs_dna['MA0013.1'], font=None)
bar.bar_data['y'] = bar.bar_data['y'] - 1.1
ggplot() + logo + bar + seqs + theme_seq() + scale_y_continuous(
    breaks=lambda x: [k + 0.5 for k in range(0, len(names))],
    labels=names)


#test_modify_the_starting_position():
names = ['seq-a', 'seq-b', 'seq-c', 'seq-d', 'seq-e', 'seq-f']
seqs = geom_alignedSeq(seqs_dna['MA0013.1'], seq_names=names)
seqs.bg_data['x'] = seqs.bg_data['x'] + 3333
seqs.letter_data['x'] = seqs.letter_data['x'] + 3333
ggplot() + seqs + theme_seq()


#test_annotate():
ggplot() + geom_alignedSeq(seqs_dna['MA0013.1']) + annotate('rect', xmin=0.5, xmax=3.5, ymin=-0.05, ymax=6.1,
                                                            alpha=.1, color='black') + theme_seq()
ggplot() + geom_seqBar(seqs_dna['MA0013.1']) + annotate('segment', x=1.5, xend=2.5, y=0, yend=0, size=2, color='red') + annotate(
    'segment', x=4.5, xend=7.5, y=0, yend=0, size=2, color='red') + annotate('segment', x=8.5, xend=11.5, y=0, yend=0,
                                                                size=2, color='red') + annotate('text', x=6, y=-0.2,
                                                                                   label='A is the most', color='red') + theme_seq()