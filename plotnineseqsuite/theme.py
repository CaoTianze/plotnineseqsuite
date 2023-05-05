from plotnine import theme_538, theme, element_rect, element_blank, element_text


def theme_seq():
    return theme(panel_grid=element_blank(),panel_background=element_rect(fill='white'))