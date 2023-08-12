import os
from pathlib import Path

# TODO: define things relative to this
root = Path(os.getenv("AFRAME_PLOT_DATA", "/"))


class DataPaths:
    """
    Once we have everything in one place,
    use this to define plots relative to
    the root location. Hard-coding in full
    paths for the time being
    """
    INTERVAL_PLOTS: Path = Path("/home/ethan.marx/aframe/interval-runs")
    MDC_RESULTS: Path = Path("/home/alec.gunny/ml-mdc/comp-results")
    AFRAME_MDC_RESULTS: Path = Path(
        "/home/alec.gunny/ml-mdc/results/hp_search_230801/"
        "GPU-2/iteration_1/evaluation.hdf"
    )

    # e.g.
    # INTERVAL_PLOTS = root / "interval-runs"
