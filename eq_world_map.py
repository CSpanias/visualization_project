import json

# import the Scattergeo chart type
from plotly.graph_objs import Scattergeo, Layout
# import offline to render the map
from plotly import offline

# explore the structure of the data
filename = 'mapping_global_data_sets/data/eq_data_30_day_m1.json'

with open(filename) as f:
    # convert JSON to dict
    all_eq_data = json.load(f)
    
# take all data associated with the key features and store them in a list
all_eq_dicts = all_eq_data['features']

# extract magnitudes, and location data
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    
    # extract magnitudes
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    
    # extract longitude
    lon = eq_dict['geometry']['coordinates'][0]
    lons.append(lon)
    
    # extract latitude
    lat = eq_dict['geometry']['coordinates'][1]
    lats.append(lat)
    
    # extract location name
    title = eq_dict['properties']['title']
    hover_texts.append(title)
    
"""
map the earthquakes
"""

# create a dict and create an object inside the list
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    # modify marker's appearance
    'marker': {
        'size': [5*mag for mag in mags],
        # where each marker falls on the colorscale
        'color': mags,
        # which range of colors to use
        'colorscale': 'Viridis',
        # brightyellow = low, dark blue = high
        'reversescale': True,
        # set title for the side colorbar
        'colorbar': {'title': 'Magnitude'},
    }
}]

# set and center a graph title
my_layout = Layout(title='Global Earthquakes', title_x=0.5)


fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')