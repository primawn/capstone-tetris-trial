import streamlit as st
import pandas as pd
import numpy as np

##STREAMLIT
st.set_page_config(layout="wide")
st.title("Prevalensi TBC Terhadap Penderita Diabetes di Pulau Jawa Pada 2020")
st.caption("Prima Widiani - TETRIS Program 2022")

with st.container():
   st.header("Latar Belakang")
with st.container():
   st.write("Kemajuan teknologi memang membawa pengaruh baik, namun di sisi lain juga membawa dampak buruk bagi manusia. Hidup yang serba mudah membuat kita seringkali menjadi lalai dalam menjaga gaya hidup dan pola makan. Menurut WHO, seperti dikutip oleh Kemkes, gaya hidup yang tidak baik tersebut merupakan salah satu pemicu diabetes melitus (Kemkes, 2018), yang mana sejauh ini penderita diabetes melitus semakin bertambah banyak.")
   st.caption("Diabetes melitus merupakan suatu penyakit yang menyebabkan gangguan metabolisme kronis pada tubuh (WHO, 1999). Hal ini menyebabkan tingginya kadar gula darah, terganggunya produksi insulin dalam tubuh, dan seringkali juga memberikan peluang bagi penyakit lain untuk masuk ke tubuh kita, salah satunya adalah TBC. Tuberkulosis (TBC/TB) adalah penyakit mudah menular yang disebabkan oleh infeksi bakteri, yang pada umumnya menyerang paru-paru.")


st.sidebar.write("Data Penderita Diabetes Melitus dan TBC per Provinsi")
st.sidebar.caption("Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa")
