import pandas as pd
import streamlit as st
import data


choice_prov = st.selectbox(
    'Data Penderita Diabetes Melitus dan TBC berdasarkan Provinsi',
    ('DKI Jakarta','Banten','DI Yogyakarta','Jawa Barat','Jawa Tengah','Jawa Timur'))

if choice_prov == "DKI Jakarta":
         st.table(data.jkt_data)
if choice_prov == "Banten":
         st.table(data.banten_data)
if choice_prov == "DI Yogyakarta":
         st.table(data.diy_data)
if choice_prov == "Jawa Barat":
         st.table(data.jabar_data)
if choice_prov == "Jawa Tengah":
         st.table(data.jateng_data)
if choice_prov == "Jawa Timur":
         st.table(data.jatim_data)

hide_jkt_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_jkt_data_row_index, unsafe_allow_html=True)

hide_diy_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_diy_data_row_index, unsafe_allow_html=True)

hide_banten_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_banten_data_row_index, unsafe_allow_html=True)

hide_jabar_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_jabar_data_row_index, unsafe_allow_html=True)

hide_jatim_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_jatim_data_row_index, unsafe_allow_html=True)

hide_jateng_data_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
st.markdown(hide_jateng_data_row_index, unsafe_allow_html=True)

st.caption("(Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa)")
