import json

# explore the structure of the data
filename = 'mapping_global_data_sets/data/eq_data_1_day_m1.json'

with open(filename) as f:
    # convert JSON to dict
    all_eq_data = json.load(f)
    
# take all data associated with the key features and store them in a list
all_eq_dicts = all_eq_data['features']
# print the length of the list
print(len(all_eq_dicts))

# extract magnitudes, and location data
mags, lons, lats = [], [], []
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
    

print(mags[:10])
print(lons[:10])
print(lats[:10])
