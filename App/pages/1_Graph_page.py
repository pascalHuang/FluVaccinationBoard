import streamlit as st
import pandas as pd
import time
from PIL import Image

# Page congiguration 
st.set_page_config(page_title="Graph page", page_icon="📈", layout="wide")

# sidebar configuration 
st.sidebar.header("Graph flu page")
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
st.markdown("<h1 style='text-align: center;'>Boarding of the evolution of the Flu symptom📈</h1>", unsafe_allow_html=True)
st.write("\n")

# Data processing
df2 = pd.read_csv(r'https://www.sentiweb.fr/datasets/incidence-PAY-3.csv', sep =',',skiprows = 1, encoding = 'iso-8859-1')
df2 = df2.sort_values(by = ['week'])
df2.reset_index(inplace=True)

def get_year(week): 
    return str(week)[:4]

df2['year'] = df2['week'].map(get_year)

def get_nweek(week): 
    return str(week)[4:6]

df2['nweek'] = df2['week'].map(get_nweek)

df2['week2'] = df2['week'].map(get_year) + ' - week '+ df2['week'].map(get_nweek)


df2.rename(columns={"week": "weektopreprocess", "week2": "week", "inc":"Estimated incidence"}, inplace=True)

st.write("## Data from [Sentinelles](https://www.sentiweb.fr/france/fr/?page=table)")
st.write("**Weekly report of flu symptom cases in France since 1984**")

# First graph
st.line_chart(df2, x="week", y=["Estimated incidence"], width=1000, use_container_width=False)
st.markdown("**Case description : Sudden onset of fever above 39°C, accompanied by mialgia and respiratory signs.**")

# Second graph
st.write("## The sum of every cases grouped by week")
dfnweek = df2.groupby(['nweek']).sum()['Estimated incidence']
st.line_chart(dfnweek,x=["nweek"], y=["Estimated incidence"], width=1000, use_container_width=False)
st.markdown("**As we can see, every year, during the winter (week 51 and week 6) we have a peak of flu contamination.**")
st.write('\n')
st.write('\n')
st.write('\n')

# Third graph
st.write("##### Let's focus on a year in particular")

year_option = df2['year'].unique().tolist()
year = st.slider('Which year you like to see?', 
                min_value=int(min(year_option))+1,
                max_value=int(max(year_option)),
                step=1)

df2 = df2[df2['year'] == str(year)]
df2.reset_index(inplace=True)

last_rows = [df2['Estimated incidence'][0]]
chart = st.line_chart(last_rows)

for i in range(1, len(df2)):
    new_rows = [df2['Estimated incidence'][i]]
    chart.add_rows(last_rows)
    last_rows = new_rows
    time.sleep(0.01)