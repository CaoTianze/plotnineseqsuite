# color schemes
Default color schemes: chemistry, chemistry2, hydrophobicity, nucleotide, nucleotide2, base_pairing, clustalx, taylor.
## *function* make_col_scheme(name: str = 'Custom Scheme', chars: Optional[list[str]] = None, groups: Optional[list[int]] = None, cols: Optional[list[int]] = None, values: Optional[list[int]] = None) -> dict
```python
from plotnineseqsuite.col_schemes import make_col_scheme
cs1 = make_col_scheme(chars=['A', 'T', 'C', 'G'], groups=['gr1', 'gr1', 'gr2', 'gr2'],cols=['purple', 'purple', 'blue', 'blue'])
cs2 = make_col_scheme(chars=['A', 'T', 'C', 'G'], values=[1,2,3,4])
```
The function is used to create custom color style themes.
### name
Name of custom scheme. It will display in legend.
### chars
Letters will used to plot.
### groups
Used in a custom discrete color scheme. It groups letters.
### cols
Used in a custom discrete color scheme. It represents the RGB value of the grouped color.
### values
Used in a custom continuous color scheme. It represents the numeric value of the corresponding letter.
## *function* get_col_scheme(col_scheme: str, seq_type: str = 'AUTO') -> dict
This function is used to get the built-in color theme of the type of the given sequence.
```python
from plotnineseqsuite.col_schemes import get_col_scheme
col_df = get_col_scheme(col_scheme='chemistry')
```
### col_scheme
One of the default color schemes.
### seq_type
AA or DNA or RNA