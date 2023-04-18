import pickle
import streamlit as st

model = pickle.load(open('Data_Tanaman_Padi_Sumatera_version_1.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Produksi Padi Di Pulau Sumatra')
st.write('---')

Tahun = st.number_input('Input Tahun(Masehi)')
Luas Panen = st.number_input('Input Luas Panen(m²)')
Curah hujan = st.number_input('Input Curah hujan (mm)')
Kelembapan = st.number_input('Input Total Kelembaban(gr)')
Suhu rata-rata = st.number_input('Input Suhu(°C )')

predict = ''

if st.button('Estimasi Produksi'):
    predict = model.predict(
        [[Tahun, Luas Panen, Curah Hujan, Kelembaban, Suhu rata-rata]]    )
    st.write ('Estimasi jumlah Produksi Padi di Pulau Sumatra (TON) : ', predict)
