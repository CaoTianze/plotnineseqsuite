import sys
from pathlib import Path
from pandas import read_csv, DataFrame

__all__ = ['times_new_roman', 'arial' , 'courier_new', 'akrobat_bold', "xkcd_regular", "akrobat_regular", "helvetica_bold", "helvetica_light", "helvetica_regular",
           "roboto_bold", "roboto_medium", "roboto_regular", "roboto_slab_bold", "roboto_slab_light",
           "roboto_slab_regular", "get_font", "list_fonts"]
data_dir = Path(__file__).parent
times_new_roman = read_csv(data_dir / 'times_new_roman.csv', index_col="index")
arial = read_csv(data_dir / 'arial.csv', index_col="index")
courier_new = read_csv(data_dir / 'courier_new.csv', index_col="index")
akrobat_bold = read_csv(data_dir / 'akrobat_bold.csv', index_col="index")
xkcd_regular = read_csv(data_dir / 'xkcd_regular.csv', index_col="index")
akrobat_regular = read_csv(data_dir / 'akrobat_regular.csv', index_col="index")
helvetica_bold = read_csv(data_dir / 'helvetica_bold.csv', index_col="index")
helvetica_light = read_csv(data_dir / 'helvetica_light.csv', index_col="index")
helvetica_regular = read_csv(data_dir / 'helvetica_regular.csv', index_col="index")
roboto_bold = read_csv(data_dir / 'roboto_bold.csv', index_col="index")
roboto_medium = read_csv(data_dir / 'roboto_medium.csv', index_col="index")
roboto_regular = read_csv(data_dir / 'roboto_regular.csv', index_col="index")
roboto_slab_bold = read_csv(data_dir / 'roboto_slab_bold.csv', index_col="index")
roboto_slab_light = read_csv(data_dir / 'roboto_slab_light.csv', index_col="index")
roboto_slab_regular = read_csv(data_dir / 'roboto_slab_regular.csv', index_col="index")


def list_fonts():
    return __all__


def get_font(font_name: str) -> DataFrame:
    if hasattr(sys.modules[__name__], font_name):
        return getattr(sys.modules[__name__], font_name)
    raise Exception("No font matches the name.")
