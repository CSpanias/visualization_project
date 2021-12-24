import csv

# import the Scattergeo chart type
from plotly.graph_objs import Scattergeo, Layout
# import offline to render the map
from plotly import offline

# explore the structure of the data
filename = 'mapping_global_data_sets/data/world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    # extract magnitudes, and location data
    mags, lons, lats = [], [], []
    for row in reader:
        # extract magnitudes
        num = float(row[2])
        mags.append(num)
        # extract longitude
        lons.append(row[1])
        # extract latitude
        lats.append(row[0])

"""
map the fires
"""

# create a dict and create an object inside the list
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    # modify marker's appearance
    'marker': {
        'size': [0.09*mag for mag in mags],
        # where each marker falls on the colorscale
        'color': mags,
        # which range of colors to use
        'colorscale': 'Viridis',
        # brightyellow = low, dark blue = high
        'reversescale': True,
        # set title for the side colorbar
        'colorbar': {'title': 'Brightness'},
    }
}]

# set and center a graph title
my_layout = Layout(title='World Fires', title_x=0.5)


fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')