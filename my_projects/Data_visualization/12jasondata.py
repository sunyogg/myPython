# import json

# from plotly.graph_objs import Scattergeo, Layout

# from plotly import offline

# filename = 'data2/eq_data_1_day_m1.json'
# readablef = 'data2/readable_eq_data_1_day_m1.json'

# with open(filename) as json_file:
#     all_eq_data = json.load(json_file)

#     with open(readablef, 'w') as json_file:
#         json.dump(all_eq_data, json_file, indent=4)

# all_eq_data = all_eq_data["features"]

# mags = []
# longs = []
# lats = []

# # inside a big dictionary there's a key called "features" which is a list of 
# # dictionaries and those dictionary have keys like 'type', 'properties', 
# # 'geometry' and those keys have values that are dicionaries like 'mag', 
# # 'place', 'time', etc.

# # element are dictionary inside 'features' list(of all_eq_data).

# # accessing those elements of json file and keeping them inside corresponding
# # list.
# for element in all_eq_data:
#     mags.append(element["properties"]["mag"])
#     longs.append(element["geometry"]["coordinates"][0])
#     # list inside a dicitionary inside a dictionary inside a dictionary.
#     lats.append(element["geometry"]["coordinates"][1])
#     # wuff! that was interesting.


# # mapping the earthquake data on world map.

# data = [Scattergeo(lon=longs, lat=lats)]
# my_layout = Layout(title='Global Earthquakes')
# fig = {'data':data, 'layout':my_layout}

# offline.plot(fig, filename='earthglobe.html')

# --------------------------------------------------------------------------------------------------------

# lis = [{'name':'sunyog', 'properties':{'height':5.11, 'weight':70}}]
# print(lis[0]['properties']['height'])

# --------------------------------------------------------------------------------------------------------

# practice set also done in this since it was easy


import json

from plotly.graph_objs import Scattergeo, Layout

from plotly import offline

filename = 'data2/eq_data_30_day_m1.json'
readablef = 'data2/readable_eq_data_30_day_m1.json'

with open(filename) as json_file:
    all_eq_data = json.load(json_file)

    with open(readablef, 'w') as json_file:
        json.dump(all_eq_data, json_file, indent=4)

#all_eq_data = all_eq_data["features"]

mags = []
longs = []
lats = []
hover_text = []

# inside a big dictionary there's a key called "features" which is a list of 
# dictionaries and those dictionary have keys like 'type', 'properties', 
# 'geometry' and those keys have values that are dicionaries like 'mag', 
# 'place', 'time', etc.

# element are dictionary inside 'features' list(of all_eq_data).

# accessing those elements of json file and keeping them inside corresponding
# list.
for element in all_eq_data["features"]:
    mags.append(element["properties"]["mag"])
    longs.append(element["geometry"]["coordinates"][0])
    # list inside a dicitionary inside a dictionary inside a dictionary.
    lats.append(element["geometry"]["coordinates"][1])
    hover_text.append(element['properties']['title'])
    # wuff! that was interesting.


main_title = all_eq_data["metadata"]["title"]

# mapping the earthquake data on world map.



data = [{
    'type':'scattergeo', # type of graph
    'lon':longs,
    'lat':lats,
    'text':hover_text, # hover text
    'marker':{
        'size':[mag * 3 for mag in mags],
        'opacity':0.3,
        'color':mags,
        'colorscale':'reds_r', # colormap
        'reversescale':True,
        'colorbar':{'title':'Magnitude'} # showing colormap on side
    }
}]
my_layout = Layout(title=main_title)
fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='earthglobe.html')



# --------------------------------------------------------------------------------------------------------