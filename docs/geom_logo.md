# geom_logo
A class that represents the sequence logo
## *Sample code*
```python
from plotnine import ggplot
from plotnineseqsuite import geom_logo, theme_seq
from plotnineseqsuite.data import seqs_dna
ggplot() + geom_logo(seqs_dna['MA0001.1']) + theme_seq()
```
## *Init param*
```
geom_logo(self,
             data: list[str] | ndarray | dict | None = None,
             method: str = 'bits',
             seq_type: str = 'AUTO',
             namespace: list[str] | None = None,
             font: str = 'roboto_medium',
             stack_width: float = 0.95,
             rev_stack_order: bool = False,
             col_scheme: DataFrame | str = 'AUTO',
             low_col: str = 'black',
             high_col: str = 'yellow',
             na_col: str = '#333333',
             **kwargs: Any) -> Any
```
- data    
Sequence data or PFM or corresponding dict.
- method    
bits, probability, custom
- seq_type    
OTHER, AA, DNA, RNA
- namespace    
The letter corresponding to the data. If the type of data is ndarray, the order of the namespaces must correspond to that of ndarray.
- font    
Font value
- stack_width    
The ratio of the size of letters to the standard unit width.
- rev_stack_order    
Order of letter stack is reversed.
- col_scheme    
Color scheme of the letters.
- low_col    
Continuous color schemes are available.
- high_col    
Continuous color schemes are available.
- na_col    
Used when the letters in the corresponding namespace do not have a color matching value defined.
- kwargs    	
Other arguments passed on to layer().
## *properties*
- data    
DataFrame.
- scale_x_continuous    
A custom scale_x_continuous.
- xlab    
A custom xlab.
- ylab    
A custom ylab.
- colscale_opts    
A custom scale_fill_gradient or custom scale_fill_manual.y