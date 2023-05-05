# font
Default fonts: times_new_roman, arial, courier_new, akrobat_bold, xkcd_regular, akrobat_regular, helvetica_bold, helvetica_light, helvetica_regular, roboto_bold, roboto_medium, roboto_regular, roboto_slab_bold, roboto_slab_light, roboto_slab_regular.
## *function* list_fonts()
Get all fonts.
## *function* get_font(font_name: str) -> DataFrame
```python
from plotnineseqsuite import get_font
f_df = get_font(font_name='times_new_roman')
```
Gets the specified font.
### font_name
Name of one of the default fonts.