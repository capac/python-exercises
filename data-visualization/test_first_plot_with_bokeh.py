from bokeh.plotting import figure, output_file, output_notebook, show
import numpy as np

# random data for scatter plot
a = 0.5
b = 3.0 + np.random.randn(100)
X = np.linspace(0, 10, 100)
Y = a * X + b

output_file('first_plot.html')
fig = figure(title='First plot', x_axis_label='X axis', y_axis_label='Y axis', width=800, height=600)
fig.scatter(X, Y, color='cornflowerblue', marker='o', size=10)

show(fig)
