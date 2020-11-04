# Radar Chart Package

This is a simple radar chart package to quickly use and visualise **radar charts** using a single function.

```python
from radar_chart.radar_chart import radar_chart
import matplotlib.pyplot as plt
import numpy as np
from random import random

labels = 'ATK STR DEF MAG RNG'.split()
values = [random()*100 for i in labels]

radar_chart(values, labels, line_color='red', fill_color='red')
plt.show()

```

<p align="center" width="100%">
    <img width="50%" src="https://raw.githubusercontent.com/awaiskhan0/radar_chart/master/output/radar_chart_example_1.png">
</p>

```python
labels = [str(i) + ":00" for i in range(1,13)][::-1]
values = [random()*1000 for i in range(len(labels))]

radar_chart(values, labels, y_ticks=False, rotate=90)
plt.show()
```

<p align="center" width="100%">
    <img width="50%" src="https://raw.githubusercontent.com/awaiskhan0/radar_chart/master/output/radar_chart_example_2.png">
</p>

### Parameters:

* `stats`: sequence of scalar
* `cat_labels`: sequence of string, default `None`. Labels for each value in `strats`
* `line_color`: string, default `#1E88E5`. Defines the line color that joins the plotted values.
* `fill_color`: string, default `#1E88E5`. Defines the fill color of the plot area.
* `marker`: string, default `None`. Marker style e.g. `+`, `x`, `o`.
* `marker_alpha`: float between 0-1, default `1`. Sets the transparency of the marker (0: Transparent, 1: Opaque).
* `fill_alpha`: float between 0-1, default `1`. Sets the transparency of the fill of the plot area (0: Transparent, 1: Opaque).
* `rotate`: float, default `'Degrees'`. Default setting does nothing. Accepts degrees (which is converted to radians) and rotates the plot clockwise.
* `reverse_rotation` bool, default `False`. Direction of the plot is reversed if `True`.
* `y_ticks` sequence of scalar/string or bool, default `True`. Default will set y-tick labels according to `stats` values. No y-tick labels if `False`. Sets sequence as y-tick labels if sequence.
* `x_ticks` sequence of scalar/string or bool, default `True`. Default will set y-tick labels according to `cat_labels` values. No y-tick labels if `False`. Sets sequence as x-tick labels if sequence.
* `gridline` bool, default `True`. Removes gridlines if `False`
* `gridline_color` string, default `'#888888'`. Defines the color of the gridlines.
* `gridline_width` float, default `0.3`. Defines the width of the gridlines.
