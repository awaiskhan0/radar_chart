import matplotlib.pyplot as plt
import numpy as np


def radar_chart(stats, cat_labels=None, line_color='#1E88E5', fill_color='#1E88E5', marker=None, marker_alpha=1,
                fill_alpha=0.25, rotate='Degrees', reverse_rotation=False, y_ticks=True, x_ticks=True, gridline=True,
                gridline_color='#888888', gridline_width=0.3):

    if cat_labels:
        labels = np.array(cat_labels)
    else:
        labels = [''] * len(stats)

    angles = np.linspace(0, 2 * np.pi, len(stats), endpoint=False)
    stats = np.concatenate((stats, [stats[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, linewidth=1, color=line_color, marker=marker, alpha=marker_alpha)
    ax.fill(angles, stats, alpha=fill_alpha, color=fill_color)
    ax.set_thetagrids(angles * 180 / np.pi, labels)

    if not gridline:
        ax.grid(False)
    else:
        ax.grid(color=gridline_color, linewidth=gridline_width)

    if rotate != 'Degrees':
        ax.set_theta_offset(rotate / 180 * np.pi)
    if reverse_rotation:
        ax.set_theta_direction(-1)

    if not y_ticks or isinstance(y_ticks, list):
        if not y_ticks:
            y_ticks = []
        ax.set_yticklabels(y_ticks)

    if not x_ticks or isinstance(x_ticks, list):
        if not x_ticks:
            x_ticks = []
        locs, lab = plt.xticks()
        plt.xticks(locs, x_ticks)