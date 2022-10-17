import streamlit as st
import pandas as pd
import numpy as np
import tabulate
import altair as alt
import matplotlib.pyplot as mp
import data
import page_1
import page_2

#STREAMLIT
#Create header
st.write("""# Hubungan Prevalensi Diabetes Melitus dengan Prevalensi TB Paru di Pulau Jawa Tahun 2020""")
st.write("Prima Widiani | Tetris Program 2022")

#image
st.image('./Java_blank_map.jpg')

PAGES = {
    "Judul": capstone
    "Latar Belakang": page_1,
    "Data per Provinsi": page_2
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
