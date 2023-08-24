# geom_alignedSeq
A class that represents the sequence alignment diagram
## *Sample code*
```python
from plotnine import ggplot, coord_fixed
from plotnineseqsuite import geom_alignedSeq, theme_seq
from plotnineseqsuite.data import seqs_dna
ggplot() + geom_alignedSeq(seqs_dna['MA0013.1']) + theme_seq() + coord_fixed()
```
## *Init param*
```
geom_alignedSeq(self,
             data: list[str] | dict | None = None,
             seq_names: list[str] | None = None,
             seq_type: str = 'AUTO',
             namespace: list[str] | None = None,
             font: str = 'roboto_medium',
             stack_width: float = 0.75,
             border_col: str = 'grey',
             scheme_applied: str = 'BACKGROUND',
             no_scheme_col: str = '#000000',
             col_scheme: DataFrame | str = 'AUTO',
             low_col: str = 'black',
             high_col: str = 'yellow',
             na_col: str = '#333333',
             **kwargs: Any) -> Any
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
- border_col
The color of the border in the background. When it is None, the border of the background will disappear.
- scheme_applied
BACKGROUND or LETTER. Indicates the target to which the color scheme applies.
- no_scheme_col    
When a color scheme is applied to the background, this indicates the color of the letters. When a color scheme is applied to letters, this indicates the color of the background.
- col_scheme    
Color scheme.
- low_col    
Continuous color schemes are available.
- high_col    
Continuous color schemes are available.
- na_col    
It is available when the corresponding namespace do not have a color matching value defined.
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