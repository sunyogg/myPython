# fire data

import csv

from plotly.graph_objects import Scattergeo, Layout

from plotly import offline


# collecting the data from csv
longs = []
lats = []
brightness = []

filename = 'data2/world_fires_7_day.csv'

with open(filename) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        longs.append(line['longitude'])
        lats.append(line['latitude'])
        brightness.append(float(line['bright_ti4']))


# plotting the data
data = [{
    'type':'scattergeo',
    'lon':longs[:1000], # decreased data size, as mac was lagging.
    'lat':lats[:1000],
    'text':brightness,
    'marker':{
        'size':[ 0.03 * x for x in brightness[:1000]],
        'opacity':0.3,
        'color':brightness,
        'colorscale':'Viridis',
        'colorbar':{'title':'Brightness'}
    }
}]
my_layout = Layout(title="Global Fire Graph")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='firegraph.html')

# print('\n')
# print(len(longs))
