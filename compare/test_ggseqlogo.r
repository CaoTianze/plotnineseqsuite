library(ggplot2)
library(ggseqlogo)
data(ggseqlogo_sample)

A=ggplot() + geom_logo(seqs_aa[['CSNK2A2']], method = 'probability', col_scheme='chemistry')+ggtitle('B')+guides(fill=FALSE)
A=A+theme(panel.grid=element_blank(),panel.background=element_rect(fill='white'),axis.ticks.x=element_blank())
ggsave('Fig. 3B.png',width=7,height=7,dpi=300)
