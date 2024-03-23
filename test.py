import pandas as pd
import plotly.express as px
import time
start = time.process_time()
df = pd.read_csv('Crimes_-_Map.csv')

df_arrests = df[df["ARREST"] == "Y"]
fig = px.scatter_mapbox(df_arrests, lat='LATITUDE', lon='LONGITUDE', hover_name=' PRIMARY_DESCRIPTION', hover_data=
['BEAT', ' SECONDARY_DESCRIPTION', 'DATE_OF_OCCURRENCE', ' LOCATION_DESCRIPTION'], zoom=10)
fig.update_layout(title='Chicago Crimes', title_x=0.5)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

shots = pd.read_csv('Violence_Reduction_-_Shotspotter_Alerts_20240307.csv')
fig = px.scatter_mapbox(shots, lat='LATITUDE', lon='LONGITUDE', hover_name='INCIDENT_TYPE_DESCRIPTION', hover_data=
['BEAT', "DATE", "ROUNDS", "COMMUNITY_AREA"], zoom=10)
fig.update_layout(title='Chicago Crimes', title_x=0.5)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

print(f"Size: {df.shape[0]}")
print(f"Time: {time.process_time() - start}")
print("test.py executed successfully!")

