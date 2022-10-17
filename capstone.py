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



#SIDEBAR
def main():
    page = st.sidebar.selectbox(
        "Navigasi",
        [
            "Judul",
            "Latar Belakang",
            "Data per Provinsi",
            "Scatter Plot",
            "Histogram",
            "Pie Chart",
            "Sub Plot"
        ]
    )

#First Page
if page == "judul":
    capstone()

#Second Page
elif page == "Latar Belakang":
    page_1()
    
#Third Page
elif page == "Data per Provinsi":
    page_2()

#Fourth Page
elif page == "Scatter Plot":
    scatter_plot()
    
#Fifth page
elif page == "Histogram":
    histogram()
    
#Sixth Page
elif page == "Pie Chart":
    pieChart()

elif page == "Sub Plot":
    subPlot()
