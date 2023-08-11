from bokeh.plotting import figure


def get_figure(**kwargs):
    default_kwargs = dict(
        height=300,
        width=700,
        tools=""
    )
    kwargs = kwargs | default_kwargs
    p = figure(**kwargs)

    if not kwargs.get("tools"):
        p.toolbar_location = None
    return p
