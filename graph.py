"""
The following line graph shows the percentage of women who have received a bachelor's degree over years in USA. The graph was produced out of the Year  and Engineering  columns of the CSV file
"""

# Import bokeh 
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.io import output_file

# Import pandas
import pandas

# Prepparate the csv data
df = pandas.read_csv("bachelors.csv")

x = df["Year"]
y = df["Engineering"]

# Writes in a html file
output_file("Bachelors graph.html")

# Create a figure object
f = figure()

# Write the plot line
f.line(x, y)

# Write the plot in the figure object
show(f)