# geom_alignedSeq
A class that represents the sequence alignment diagram
## *class* geom_alignedSeq(self,data: Union[list[str], dict, None] = None,seq_names: Optional[list[str]] = None,seq_type: str = 'AUTO',namespace: Optional[list[str]] = None,font: str = 'roboto_medium',stack_width: float = 0.75,font_col: str = '#FFFFFF',bg_col_scheme: Union[DataFrame, str] = 'AUTO',bg_low_col: str = 'black',bg_high_col: str = 'yellow',bg_na_col: str = '#333333',**kwargs: Any)
```python
from plotnine import ggplot, coord_fixed
from plotnineseqsuite import geom_alignedSeq, theme_seq
from plotnineseqsuite.data import seqs_dna
ggplot() + geom_alignedSeq(seqs_dna['MA0013.1']) + theme_seq() + coord_fixed()
```
- data    
Sequence data or corresponding dict.
- seq_names    
The name corresponding to the sequence data.
- seq_type    
OTHER, AA, DNA, RNA
- namespace    
The letter corresponding to the data. 
- font    
Font value
- stack_width    
The ratio of the size of letters to the standard unit width.
- font_col    
The color of the font.
- bg_col_scheme    
Color scheme of the backgrounds.
- bg_low_col    
Continuous color schemes are available.
- bg_high_col    
Continuous color schemes are available.
- bg_na_col    
Used when the background in the corresponding namespace do not have a color matching value defined.
- kwargs    
Other arguments passed on to layer().
## *properties*
- bg_data    
DataFrame.
- letter_data    
DataFrame.
- scale_x_continuous    
A custom scale_x_continuous.
- scale_y_continuous    
A custom scale_y_continuous.
- xlab    
A custom xlab.
- ylab    
A custom ylab.
- colscale_opts    
A custom scale_fill_gradient or custom scale_fill_manual.