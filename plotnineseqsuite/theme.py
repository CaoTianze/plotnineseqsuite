from plotnine import theme, element_rect, element_blank


class theme_seq:
    def __init__(self):
        pass

    def __radd__(self, gg):
        gg += theme(panel_grid=element_blank(), panel_background=element_rect(fill='white'))
        return gg