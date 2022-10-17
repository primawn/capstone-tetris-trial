import streamlit as st
import pandas as pd
import numpy as np
import tabulate
import altair as alt
import data
import map

#STREAMLIT
#Create header
st.write("""# Hubungan Prevalensi Diabetes Melitus dengan Prevalensi TB Paru di Pulau Jawa Tahun 2020""")
st.write("Prima Widiani | Tetris Program 2022")

# df = pd.DataFrame(data.datajawa)
# df = df.set_index('Provinsi')
chart_data = pd.DataFrame(
    data.datajawa,
    columns=["Penderita Tuberkulosis", "Penderita Diabetes"],
    index=data.datajawa['Provinsi']    
)

st.bar_chart(chart_data)

# data = pd.melt(chart_data.reset_index(), id_vars=["index"])
# chart = (
#     alt.Chart(data)
#     .mark_bar()
#     .encode(
#         x=alt.X("value", type="quantitative", title=""),
#         y=alt.Y("index", type="nominal", title=""),
#         color=alt.Color("variable", type="nominal", title=""),
#         order=alt.Order("variable", sort="descending"),
#     )
# )

# st.altair_chart(chart, use_container_width=True)
#image
# st.image('./Java_blank_map.jpg')
# st.write(data_all['Provinsi'])

# st.write("""Latar Belakang""")
st.write("Hidup yang menjadi lebih mudah di kemajuan teknologi ini membuat kita seringkali menjadi lalai dalam menjaga gaya hidup dan pola makan. Menurut WHO, gaya hidup yang tidak baik tersebut merupakan salah satu pemicu diabetes melitus (Kemkes, 2018), yang mana sejauh ini penderita diabetes melitus semakin bertambah banyak.")
st.caption("Diabetes melitus merupakan suatu penyakit yang menyebabkan gangguan metabolisme kronis pada tubuh (WHO, 1999). Hal ini menyebabkan tingginya kadar gula darah, terganggunya produksi insulin dalam tubuh, dan seringkali juga memberikan peluang bagi penyakit lain untuk masuk ke tubuh kita, salah satunya adalah TBC. Tuberkulosis (TBC/TB) adalah penyakit mudah menular yang disebabkan oleh infeksi bakteri, yang pada umumnya menyerang paru-paru.")

# st.table(data.datajawa)

# #chart
# alt.data_transformers.disable_max_rows()

# np.random.seed(0)
# data = pd.DataFrame({
#     'Jumlah': pd.date_range('1990-01-01', freq='Y', periods=10),
#     'FAO_yied': np.random.randn(10).cumsum(),
#     'Simulation': np.random.randn(10).cumsum(),
#     'Predicted': np.random.randn(10).cumsum()
# })

# # data_jawa = pd.melt(data, id_vars=['date'], value_vars=['FAO_yied', 'Predicted', 'Simulation'])
# chart = alt.Chart(data.datajawa, title='Jumlah penderita DM dan TB di Pulau Jawa 2020 berdasarkan Provinsi').mark_bar(
#     opacity=1,
#     ).encode(
#     column = alt.Column('date:O', spacing = 5, header = alt.Header(labelOrient = "bottom")),
#     x =alt.X('Kabupaten/Kota', sort = ["Penderita Tuberkulosis", "Penderita Diabetes"],  axis=None),
#     y =alt.Y('value:Q'),
#     color= alt.Color('variable')
# ).configure_view(stroke='transparent')

# chart.display() 

st.write("Persebaran "+map.select_data+' di Pulau Jawa')
map.show_maps(map.select_data, map.threshold(map.select_data))

choice_prov = st.sidebar.selectbox(
    'Data Penderita Diabetes Melitus dan TBC berdasarkan Provinsi',
    ('Semua Data', 'DKI Jakarta','Banten','DI Yogyakarta','Jawa Barat','Jawa Tengah','Jawa Timur'))

if choice_prov == "Semua Data":
         st.sidebar.table(data.datajawa)
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
