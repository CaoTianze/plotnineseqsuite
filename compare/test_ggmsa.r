library(ggseqlogo)
library(Biostrings)
data(ggseqlogo_sample)
library(ggplot2)
library(ggmsa)
aastr=seqs_aa[['CSNK2A2']]
names(aastr)=1:80
seqstr = AAStringSet(aastr)

A=seqlogo(seqstr, adaptive = TRUE)+ggtitle('C')
A=A+theme(panel.grid=element_blank(),panel.background=element_rect(fill='white',color=NA),plot.background=element_rect(fill='white',color=NA),axis.ticks.x=element_blank())
ggsave('Fig. 3C.png',width=7,height=7,dpi=300)
