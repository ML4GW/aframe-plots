import numpy as np
from bokeh.plotting import figure
from bokeh.palettes import Bright7 as palette  # noqa


subscripts = {}
for i in range(10):
    subscripts[i] = rf"\u{2080 + i}".encode().decode("unicode-escape")


def get_figure(**kwargs):
    default_kwargs = dict(
        height=300,
        width=700,
        tools=""
    )
    kwargs = default_kwargs | kwargs
    p = figure(**kwargs)

    if not kwargs.get("tools"):
        p.toolbar_location = None

    title = kwargs.get("title")
    if title and title.startswith("$$"):
        p.title.text_font_style = "normal"
    return p


def hide_axis(p, axis) -> None:
    axis = getattr(p, axis + "axis")
    axis.major_tick_line_color = None
    axis.minor_tick_line_color = None

    # can't set this to 0 otherwise log-axis
    # plots freak out and won't render
    axis.major_label_text_font_size = "1pt"
    axis.major_label_text_color = None


def plot_err_bands(p, x, y, err, **kwargs):
    return p.patch(
        np.concatenate([x, x[::-1]]),
        np.concatenate([(y - err), (y + err)[::-1]]),
        **kwargs
    )
