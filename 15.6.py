from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create two D8 die
die_1 = Die(8)
die_2 = Die(8)

# make some rolls, and store results in a list
results = []
for roll_num in range(1_000):
    # sum of the 2 rolls
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
# define maximum value the sum of the 2 die sides
max_result = die_1.num_sides + die_2.num_sides
# define minimum values as the minimun number of the list
min_result = min(results)
# for the number 1 to 13
for value in range(min_result, max_result+1):
    # count the times that each number appears in the list
    frequency = results.count(value)
    frequencies.append(frequency)

""" visualize the results """

"""
plotly does not accept the range() directly, so we need to convert it to a list
"""
# store the sides of the 2 dice (2-13)
x_values = list(range(2, max_result+1))
# formatted as a BarChart, [] because can have multiple elements
data = [Bar(x=x_values, y = frequencies)]

"""
dtick key controls the spacing of tick marks. With more Bars on the histogram,
Plotly's def settings will only label some of the bars. Setting 'dtick': 1 tells
Plotly to label every tick mark.
"""
# each config option is stored as an entry in a dictionary
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

# returns an object that specifies the layout and config of the graph as a whole
my_layout = Layout(title='Results of rolling two D8 die 1,000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)

# a dictionary containing the data and layout objects, file name
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
