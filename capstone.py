import streamlit as st
import pandas as pd
import numpy as np
import tabulate
import altair as alt
import matplotlib.pyplot as mp

#STREAMLIT
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
hide_jkt_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_jkt_data_row_index, unsafe_allow_html=True)

##DIY
diy_data = pd.read_csv('./Capstone Project/DI_Yogya.csv', sep=';')
diy_data = diy_data.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','TB':'Jumlah Penderita TB','DM':'Jumlah Penderita DM'})
hide_diy_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_diy_data_row_index, unsafe_allow_html=True)

##BANTEN
banten_dm = pd.read_csv('./Capstone Project/DM_Banten.csv', sep=',')
banten_dm = banten_dm.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','Jumlah_Penderita_DM':'Jumlah Penderita DM'})
banten_dm = banten_dm.drop(labels=['Puskesmas'], axis=1)
banten_tb = pd.read_csv('./Capstone Project/TB_Banten.csv', sep=',')
banten_tb = banten_tb.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','Total_Penderita':'Jumlah Penderita TB'})
banten_tb = banten_tb.drop(labels=['Puskesmas','Penderita_Laki','Penderita_Perempuan'], axis=1)
banten_data = pd.merge(banten_tb,banten_dm)
hide_banten_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_banten_data_row_index, unsafe_allow_html=True)

##JABAR
jabar_dm = pd.read_csv('./Capstone Project/DM_Jawa_Barat.csv', sep=';')
jabar_dm = jabar_dm.rename(columns={'Kecamatan_Kota':'Kabupaten/Kota','Jumlah_Penderita_DM':'Jumlah Penderita DM'})
jabar_tb = pd.read_csv('./Capstone Project/TB_Jawa_Barat.csv', sep=';')
jabar_tb = jabar_tb.rename(columns={'Kecamatan_Kota':'Kabupaten/Kota','Total_Penderita':'Jumlah Penderita TB'})
jabar_tb = jabar_tb.drop(labels=['Penderita_Laki','Penderita_Perempuan'], axis=1)
jabar_data = pd.merge(jabar_tb,jabar_dm)
hide_jabar_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_jabar_data_row_index, unsafe_allow_html=True)

##JATIM
jatim_data = pd.read_csv('./Capstone Project/Jawa_Timur.csv', sep=';')
jatim_data = jatim_data.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','TB':'Jumlah Penderita TB','DM':'Jumlah Penderita DM'})
hide_jatim_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_jatim_data_row_index, unsafe_allow_html=True)

##JATENG
jateng_data = pd.read_csv('./Capstone Project/Jawa_Tengah.csv', sep=';')
jateng_data = jateng_data.rename(columns={'Kabupaten_Kota':'Kabupaten/Kota','TB':'Jumlah Penderita TB','DM':'Jumlah Penderita DM'})
hide_jateng_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_jateng_data_row_index, unsafe_allow_html=True)

##MERGED
jawa_1 = jkt_data.append(diy_data)
jawa_2 = jawa_1.append(banten_data)
jawa_3 = jawa_2.append(jabar_data)
jawa_4 = jawa_3.append(jateng_data)
jawa_data = jawa_4.append(jatim_data)
jawa_data

##SUM
# JKT
sum_dm_jkt = jkt_data['Jumlah Penderita DM'].sum()
sum_tb_jkt = jkt_data['Jumlah Penderita TB'].sum()
# Banten
sum_dm_btn = banten_data['Jumlah Penderita DM'].sum()
sum_tb_btn = banten_data['Jumlah Penderita TB'].sum()
# DIY
sum_dm_diy = diy_data['Jumlah Penderita DM'].sum()
sum_tb_diy = diy_data['Jumlah Penderita TB'].sum()
# Jabar
sum_dm_jabar = jabar_data['Jumlah Penderita DM'].sum()
sum_tb_jabar = jabar_data['Jumlah Penderita TB'].sum()
# Jateng
sum_dm_jateng = jateng_data['Jumlah Penderita DM'].sum()
sum_tb_jateng = jateng_data['Jumlah Penderita TB'].sum()
# Jatim
sum_dm_jatim = jatim_data['Jumlah Penderita DM'].sum()
sum_tb_jatim = jatim_data['Jumlah Penderita TB'].sum()
# Tabel per provinsi
datajawa = {'Provinsi':['DKI Jakarta','Banten','DI Yogyakarta','Jawa Barat','Jawa Tengah','Jawa Timur'], 'Penderita Tuberkulosis':[sum_tb_jkt,sum_tb_btn,sum_tb_diy,sum_tb_jabar,sum_tb_jateng,sum_tb_jatim], 'Penderita Diabetes':[sum_dm_jkt,sum_dm_btn,sum_dm_diy,sum_dm_jabar,sum_dm_jateng,sum_dm_jatim]}
hide_datajawa_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_datajawa_row_index, unsafe_allow_html=True)
st.table(datajawa)




#SIDEBAR

#adding a selectbox
choice_prov = st.sidebar.selectbox(
    'Data Penderita Diabetes Melitus dan TBC berdasarkan Provinsi',
    ('DKI Jakarta','Banten','DI Yogyakarta','Jawa Barat','Jawa Tengah','Jawa Timur'))

if choice_prov == "DKI Jakarta":
         st.sidebar.table(jkt_data, ascending True)
if choice_prov == "Banten":
         st.sidebar.table(banten_data)
if choice_prov == "DI Yogyakarta":
         st.sidebar.table(diy_data)
if choice_prov == "Jawa Barat":
         st.sidebar.table(jabar_data)
if choice_prov == "Jawa Tengah":
         st.sidebar.table(jateng_data)
if choice_prov == "Jawa Timur":
         st.sidebar.table(jatim_data)
         
st.sidebar.caption("(Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa)")
