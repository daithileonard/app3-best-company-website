import streamlit as st
import pandas
from PIL import Image

st.set_page_config(layout="wide")
st.header("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Bibendum enim facilisis gravida neque convallis a cras semper. A iaculis at erat pellentesque adipiscing. 
Tempor orci eu lobortis elementum nibh tellus. Adipiscing at in tellus integer. 
Dui id ornare arcu odio ut sem nulla pharetra diam. Nunc scelerisque viverra mauris in aliquam sem. 
Maecenas ultricies mi eget mauris pharetra et ultrices neque. Pellentesque pulvinar pellentesque habitant morbi. 
Sem fringilla ut morbi tincidunt augue. Quam id leo in vitae turpis massa sed elementum.
"""
st.write(content)
st.subheader("Our Team")

df = pandas.read_csv("data.csv")

col1, empty_col1, col2, empty_col2, col3 = st.columns(5)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])



st.write(name)
