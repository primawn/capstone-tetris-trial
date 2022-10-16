
choice_prov = st.selectbox(
    'Data Penderita Diabetes Melitus dan TBC berdasarkan Provinsi',
    ('DKI Jakarta','Banten','DI Yogyakarta','Jawa Barat','Jawa Tengah','Jawa Timur'))

if choice_prov == "DKI Jakarta":
         st.table(jkt_data)
if choice_prov == "Banten":
         st.table(banten_data)
if choice_prov == "DI Yogyakarta":
         st.table(diy_data)
if choice_prov == "Jawa Barat":
         st.table(jabar_data)
if choice_prov == "Jawa Tengah":
         st.table(jateng_data)
if choice_prov == "Jawa Timur":
         st.table(jatim_data)
         
st.caption("(Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa)")
