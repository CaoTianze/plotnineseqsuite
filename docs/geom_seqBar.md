# geom_seqBar
A class that represents the sequence histogram
## *Sample code*
```python
from plotnine import ggplot
from plotnineseqsuite import geom_seqBar, theme_seq
from plotnineseqsuite.data import seqs_dna
ggplot() + geom_seqBar(seqs_dna['MA0013.1']) + theme_seq()
```
## *Init param*
```
geom_seqBar(self,
             data: list[str] | ndarray | dict | None = None,
             seq_type: str = 'AUTO',
             namespace: list[str] | None = None,
             font: str = 'roboto_medium',
             stack_width: float = 0.75,
             bar_col_scheme: Dict | str = 'AUTO',
             font_col: str = '#808080',
             low_col: str = 'black',
             high_col: str = 'yellow',
             na_col: str = '#333333',
             **kwargs: Any) -> Any
```
- data    
Sequence data or PFM or corresponding dict.
- seq_type    
OTHER, AA, DNA, RNA
- namespace    
The letter corresponding to the data. If the type of data is ndarray, the order of the namespaces must correspond to that of ndarray.
- font    
Font value
- stack_width    
The ratio of the size of letters and the width of  bars to the standard unit width.
- bar_col_scheme    
Color scheme of the cylinder.
- font_col    
The color of the font.
- low_col    
Continuous color schemes are available.
- high_col    
Continuous color schemes are available.
- na_col    
Used when the letters in the corresponding namespace do not have a color matching value defined.
- kwargs    
Other arguments passed on to layer().
## *properties*
- bar_data    
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