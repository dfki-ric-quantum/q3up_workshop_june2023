from itertools import product

import numpy as np
import matplotlib.pyplot as plt

DARK_BLUE = '#00326D'
MID_BLUE = '#0068B4'


def sample_histogram(samples: np.ndarray) -> None:
    """Plot histogram for measurement samples.

    Parameters
    ----------
    samples: np.ndarray
        The measurement results as returned from `qml.sample()`
    """
    n_samples = samples.shape[0]
    n_dim = 1

    if len(samples.shape) == 2:
        n_dim = samples.shape[1]

    labels = [f"|{''.join(label)}>" for label in product(['0', '1'], repeat=n_dim)]
    c_samples = [f"|{''.join(sample)}>" for sample in samples.astype(int).astype(str)]
    counts = np.unique(c_samples, return_counts=True)

    bars = np.zeros(2**n_dim)

    for idx, label in enumerate(labels):
        pos = np.where(counts[0] == label)[0]

        if len(pos):
            bars[idx] = counts[1][pos[0]]

    xticks = list(range(2**n_dim))

    _, ax = plt.subplots(1, 1)
    ax.bar(xticks, bars, color=MID_BLUE, edgecolor=DARK_BLUE)
    ax.set_xticks(xticks)
    ax.set_xticklabels(labels, rotation=-90)
    ax.set_title("State histogram")
    ax.set_xlabel("State")
    ax.set_ylabel("No. of Samples")
