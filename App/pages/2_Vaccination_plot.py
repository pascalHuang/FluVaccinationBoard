import streamlit as st
import pandas as pd
from geopy.geocoders import BANFrance
import time

from PIL import Image

# Page config
st.set_page_config(page_title="Map plot", page_icon="🗺", layout="wide")

# Sidebas config
st.sidebar.header("Vaccination plot")
st.sidebar.write("### Application made by the data scientist Huang Pascal")
col1, col2, col3 = st.sidebar.columns(3)
with col1:
    st.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=50)
    st.image("https://cdn-icons-png.flaticon.com/512/174/174857.png", width=50)

with col2:
    st.write("## [🔗Github](https://github.com/pascalHuang)")
    st.write("## [🔗Linkedin](https://www.linkedin.com/in/huang-pascal/)")

img = Image.open('.\images\qr-code.png')
st.sidebar.image(img, width=200)

# Title
st.markdown("<h1 style='text-align: center;'>Where can I get vaccinated from flu in France? 💉</h1>", unsafe_allow_html=True)
st.write("\n")
st.write("## Data from [Data gouv](https://www.data.gouv.fr/fr/datasets/lieux-de-vaccination-contre-la-grippe-pharmacies-sante-fr/)")

# Processing the data
df = pd.read_csv('flu_vaccination.csv', sep=',')

df_location = pd.DataFrame(data=df[['Adresse_longitude', 'Adresse_latitude', 'region']])
df_location.dropna(inplace= True)
df_location.reset_index(inplace = True)
df_location.rename(columns={"Adresse_longitude": "lon", "Adresse_latitude": "lat"}, inplace = True)

# Reverse geocoding the location
# rerun the notebook Gripp Data.ipynb


# Regions are stored in the column "region"
st.dataframe(df_location.groupby(['region']).count().sort_values(by=['index'], ascending=False)['index'], width=400)


df_location["latitude"] = pd.to_numeric(df_location["lat"], downcast="float")
df_location["longitude"] = pd.to_numeric(df_location["lon"], downcast="float")

# Plot by region
region = df_location['region'].unique().tolist()
region.insert(0, "all region")

option = st.selectbox(
    'Which region do you want to plot?',
    region)

if option == "all region":
    st.map(df_location[['lon', 'lat']])
else:
    st.map(df_location[df_location.region == option][['lon', 'lat']])

st.write("###### Every red dot is a place where you can get vaccinated from flu.")
