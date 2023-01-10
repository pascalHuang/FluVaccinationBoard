import streamlit as st
from PIL import Image

# Page congiguration 
st.set_page_config(page_title="Welcome page", page_icon="👋", layout="wide")

# sidebar configuration 
st.sidebar.header("General information")
st.sidebar.write("### Application made by the data scientist Huang Pascal")
col1, col2, col3 = st.sidebar.columns(3)
with col1:
    st.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=50)
    st.image("https://cdn-icons-png.flaticon.com/512/174/174857.png", width=48)

with col2:
    st.write("## [🔗Github](https://github.com/pascalHuang)")
    st.write("## [🔗Linkedin](https://www.linkedin.com/in/huang-pascal/)")

img = Image.open('.\images\qr-code.png')
st.sidebar.image(img, width=200)

# Title 
st.markdown("<h1 style='text-align: center;'>Welcome the Fluboarding app 👋</h1>", unsafe_allow_html=True)
st.write("\n")

# Page content
st.write("## What is the flu ?")
col1, col2 = st.columns(2)
with col2:
    st.markdown('**Influenza**, commonly known as "**the flu**", is an infectious disease caused by influenza viruses. Symptoms range from mild to severe and often include fever, runny nose, sore throat, muscle pain, headache, coughing, and fatigue. These symptoms begin from one to four days after exposure to the virus (typically two days) and last for about 2–8 days. Diarrhea and vomiting can occur, particularly in children. Influenza may progress to pneumonia, which can be caused by the virus or by a subsequent bacterial infection.')
    st.markdown('More information : https://en.wikipedia.org/wiki/Influenza')

with col1:
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/EM_of_influenza_virus.jpg/260px-EM_of_influenza_virus.jpg', width = 400)
    st.write('*Influenza virus, magnified approximately 100,000 times*')

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<h2 style='text-align: center; color: darkblue; background: lightblue'>2 to 6 million people affected by the flu each year in France</h2>", unsafe_allow_html=True)
with col2:
    st.markdown("<h2 style='text-align: center; color: darkblue; background: lightyellow'>~ 10,000 deaths each year in France due to the Flu</h2>", unsafe_allow_html=True)
with col3:
    st.markdown("<h2 style='text-align: center; color: darkblue; background: lightpink'>+ 90% of deaths occur in people aged 65 or over</h2>", unsafe_allow_html=True)

st.write("\n")
st.write("\n")
st.write("\n")

st.write("## How to protect ourselve against the flu?")
st.image('https://a4f5cce20b1af32cb9d8-3b0202f93d305215d3d2a0852a0061c4.ssl.cf1.rackcdn.com/article/image/38770/large_flu.jpg', width = 1000)
