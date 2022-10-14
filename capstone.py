import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
#Create header
st.write("""# Prevalensi TBC Terhadap Penderita Diabetes di Pulau Jawa Pada 2020""")
st.write("Prima Widiani | Tetris Program 2022")
st.write("""## Latar Belakang""")
st.write("Hidup yang dimudahkan oleh kemajuan teknologi saat ini membuat kita seringkali menjadi lalai dalam menjaga gaya hidup dan pola makan."
         " Menurut WHO, gaya hidup yang tidak baik merupakan salah satu pemicu diabetes melitus (Kemkes, 2018), dimana penderita diabetes melitus sejauh ini semakin bertambah banyak.")
st.caption("Diabetes melitus merupakan suatu penyakit yang menyebabkan gangguan metabolisme kronis pada tubuh (WHO, 1999). Hal ini menyebabkan tingginya kadar gula darah, terganggunya produksi insulin dalam tubuh, dan seringkali juga memberikan peluang bagi penyakit lain untuk masuk ke tubuh kita, salah satunya adalah TBC."
           " Tuberkulosis (TBC/TB) sendiri adalah penyakit mudah menular yang disebabkan oleh infeksi bakteri, yang pada umumnya menyerang paru-paru.")

#image
st.image('./Java_blank_map.jpg')

st.sidebar.write("Data Penderita Diabetes Melitus dan TBC per Provinsi")
st.sidebar.caption("Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa")

datadiy = pd.read_csv('./Capstone Project/DI_Yogya.csv', sep=';')
datadiy = datadiy.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','TB':'Jumlah Penderita TB','DM':'Jumlah Penderita DM'})
st.write("## THE DATA BEING USED")
data
st.sidebar.altair_chart(datadiy)
