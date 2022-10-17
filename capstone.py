import streamlit as st
import pandas as pd
import numpy as np
import tabulate
import altair as alt
import matplotlib.pyplot as mp
import data




#STREAMLIT

choice_prov = st.sidebar.selectbox(
    'Data Penderita Diabetes Melitus dan TBC berdasarkan Provinsi',
    ('DKI Jakarta','Banten','DI Yogyakarta','Jawa Barat','Jawa Tengah','Jawa Timur'))

if choice_prov == "DKI Jakarta":
         st.sidebar.table(data.jkt_data)
if choice_prov == "Banten":
         st.sidebar.table(data.banten_data)
if choice_prov == "DI Yogyakarta":
         st.sidebar.table(data.diy_data)
if choice_prov == "Jawa Barat":
         st.sidebar.table(data.jabar_data)
if choice_prov == "Jawa Tengah":
         st.sidebar.table(data.jateng_data)
if choice_prov == "Jawa Timur":
         st.sidebar.table(data.jatim_data)
         
st.sidebar.caption("(Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa)")

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
         

