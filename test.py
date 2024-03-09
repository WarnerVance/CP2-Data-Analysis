import pandas as pd
import plotly.express as px

df = pd.read_csv('Crimes_-_Map.csv')

df_arrests = df[df["ARREST"] == "Y"]

fig = px.scatter_mapbox(df_arrests, lat='LATITUDE', lon='LONGITUDE', hover_name=' PRIMARY_DESCRIPTION', hover_data=
['BEAT', ' SECONDARY_DESCRIPTION', 'DATE_OF_OCCURRENCE'], zoom=10)
fig.update_layout(title='Chicago Crimes', title_x=0.5)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig.show()
