import streamlit as st
import pandas as pd
import numpy as np

#STREAMLIT
st.set_page_config(layout="wide")
#Create header
st.write("""# Hubungan Prevalensi Diabetes Melitus dengan Prevalensi TB Paru di Pulau Jawa Tahun 2020""")
st.write("Prima Widiani | Tetris Program 2022")
st.write("""## Latar Belakang""")
st.write("Hidup yang dimudahkan oleh kemajuan teknologi saat ini membuat kita seringkali menjadi lalai dalam menjaga gaya hidup dan pola makan."
         " Menurut WHO, hal-hal tersebut merupakan salah satu pemicu diabetes melitus (Kemkes, 2018), dimana penderita diabetes melitus sejauh ini semakin bertambah banyak.")
st.caption("Diabetes melitus merupakan suatu penyakit yang menyebabkan gangguan metabolisme kronis pada tubuh (WHO, 1999). Hal ini menyebabkan tingginya kadar gula darah, terganggunya produksi insulin dalam tubuh, dan seringkali juga memberikan peluang bagi penyakit lain untuk masuk ke tubuh kita, salah satunya adalah TBC."
           " Tuberkulosis (TBC/TB) sendiri adalah penyakit mudah menular yang disebabkan oleh infeksi bakteri, yang pada umumnya menyerang paru-paru.")

#image
st.image('./Java_blank_map.jpg')


#DATA
##JKT
jkt_tb = pd.read_csv('./Capstone Project/TB_DKI_Jakarta.csv')
jkt_tb1 = jkt_tb.drop(labels=['Puskesmas', 'Penderita_Laki','Penderita_Perempuan'], axis=1)
jkt_tb1 = jkt_tb1.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','Total_Penderita':'Jumlah Penderita TB'})

jkt_dm = pd.read_csv('./Capstone Project/DM_DKI_Jakarta.csv')
jkt_dm1 = jkt_dm.drop(labels=['Puskesmas'], axis=1)
jkt_dm1 = jkt_dm1.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','Jumlah_Penderita_DM':'Jumlah Penderita DM'})

jkt_data = pd.merge(jkt_tb1,jkt_dm1)


##DIY
diy_data = pd.read_csv('./Capstone Project/DI_Yogya.csv', sep=';')
diy_data = diy_data.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','TB':'Jumlah Penderita TB','DM':'Jumlah Penderita DM'})

##BANTEN
banten_dm = pd.read_csv('./Capstone Project/DM_Banten.csv', sep=',')
banten_dm = banten_dm.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','Jumlah_Penderita_DM':'Jumlah Penderita DM'})
banten_dm = banten_dm.drop(labels=['Puskesmas'], axis=1)

banten_tb = pd.read_csv('./Capstone Project/TB_Banten.csv', sep=',')
banten_tb = banten_tb.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','Total_Penderita':'Jumlah Penderita TB'})
banten_tb = banten_tb.drop(labels=['Puskesmas','Penderita_Laki','Penderita_Perempuan'], axis=1)




st.sidebar.write("Data Penderita Diabetes Melitus dan TBC per Provinsi")
st.sidebar.caption("Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa")
st.sidebar.altair_chart(jkt_data)
