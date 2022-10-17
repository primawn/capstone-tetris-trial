import streamlit as st
import pandas as pd
import numpy as np
import tabulate
import altair as alt
import matplotlib.pyplot as mp
import data


page_1 = open("pages/page_1.py")
page_2 = open("pages/page_2.py")

#STREAMLIT
#Create header
st.write("""# Hubungan Prevalensi Diabetes Melitus dengan Prevalensi TB Paru di Pulau Jawa Tahun 2020""")
st.write("Prima Widiani | Tetris Program 2022")

#image
st.image('./Java_blank_map.jpg')

#Sidebar
navigation = st.sidebar.selectbox(
    'Navigasi',
    ('Judul','Latar Belakang','Data per Provinsi','Jawa Barat','Jawa Tengah','Jawa Timur'))

if navigation == "Judul":
         st.sidebar.table(jkt_data)
if navigation == "Banten":
         st.sidebar.table(banten_data)
if navigation == "DI Yogyakarta":
         st.sidebar.table(diy_data)
if navigation == "Jawa Barat":
         st.sidebar.table(jabar_data)
if navigation == "Jawa Tengah":
         st.sidebar.table(jateng_data)
if navigation == "Jawa Timur":
         st.sidebar.table(jatim_data)
         

