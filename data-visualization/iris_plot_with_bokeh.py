import pandas as pd
import numpy as np
import os
from pathlib import Path
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, HoverTool

home = os.environ['HOME']
data_dir = Path(home) / 'seaborn-data'
iris_df = pd.read_csv(data_dir / 'iris.csv')

output_file('sepal_length_vs_petal_length.html')

tooltips = [('Species', '@species'),
            ('Sepal Length', '@sepal_length'),
            ('Sepal Width', '@sepal_width'),
            ('Petal Length', '@petal_length'),
            ('Petal Width', '@petal_width')
            ]

fig = figure(title='Sepal length versus petal length', x_axis_label='Sepal length (cm)',
             y_axis_label='Petal length (cm)', width=800, height=600)

iris_source = ColumnDataSource(iris_df)
color_mapper = CategoricalColorMapper(factors=np.unique(
    iris_df.species), palette=['royalblue', 'gold', 'limegreen'])
fig.circle(x='sepal_length', y='petal_length', source=iris_source, color=dict(
    field='species', transform=color_mapper), size=10, alpha=0.8, legend_field='species')
fig.add_tools(HoverTool(tooltips=tooltips))
fig.toolbar_location = 'above'

show(fig)
