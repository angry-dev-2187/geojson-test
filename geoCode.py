import json
from shapely.geometry import shape, Point

with open('19204__8_r_2024.geojson', 'r', encoding='utf-8') as file:
    data = json.load(file)    

lon = float(input("Enter longitude: "))
lat = float(input("Enter latitude: "))
print(f"Added point: ({lon}, {lat})")

point = Point(lon, lat)
for feature in data['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        properties =  feature['properties']
        print('Found containing polygon:', properties['市区町村名'], properties['大字名'], properties['丁目名'], properties['地番'])        