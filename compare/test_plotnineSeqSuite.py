from plotnine import ggplot, ggtitle, theme, guides, element_blank, element_rect
from plotnineseqsuite.data import seqs_aa
from plotnineseqsuite.logo import geom_logo

A=ggplot() + geom_logo(seqs_aa['CSNK2A2'], method='probability', col_scheme='chemistry') + ggtitle('A')+ guides(fill=False)
A=A+theme(panel_grid=element_blank(),panel_background=element_rect(fill='white'),axis_ticks_major_x=element_blank())

A.save("Fig. 3A.png",width=7,height=7,dpi=300)
