import folium as fl
import pandas as pd
map = fl.Map(zoom_start=2,max_bounds=True,location=(40.866667,34.566667))
fg1 = fl.FeatureGroup(name="Volcanoes")
fg2 = fl.FeatureGroup(name="Population")

def colour(ele):
    if ele<1000:
        return "green"
    elif 1000<= ele < 3000:
        return "orange"
    else:
        return "red"

fg2.add_child(fl.GeoJson(data=(open("world.json","r",encoding="utf-8-sig").read()),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<= x['properties']['POP2005'] <20000000 else 'red'}))
data = pd.read_csv("4.1 Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])
for la,lo,e in zip(lat,lon,ele):
    fg1.add_child(fl.CircleMarker(location=(la,lo),radius=5,popup=str(e)+" m",fill_color=colour(e),fill_opacity=0.7))
    






map.add_child(fg2)
map.add_child(fg1)

map.add_child(fl.LayerControl())
map.save(outfile="map.html")