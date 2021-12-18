from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create a D6
die = Die()

# make some rolls, and store results in a list
results = []
for roll_num in range(1_000):
    result = die.roll()
    results.append(result)

# analyze the results
frequencies = []
# for the number 1 to 7
for value in range(1, die.num_sides+1):
    # count the times that each number appears in the list
    frequency = results.count(value)
    frequencies.append(frequency)

""" visualize the results """

"""
plotly does not accept the range() directly, so we need to convert it to a list
"""
# store the sides of the die
x_values = list(range(1, die.num_sides+1))
# formatted as a BarChart, [] because can have multiple elements
data = [Bar(x=x_values, y = frequencies)]

# each config option is stored as an entry in a dictionary
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

# returns an object that specifies the layout and config of the graph as a whole
my_layout = Layout(title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)

# a dictionary containing the data and layout objects, file name
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
