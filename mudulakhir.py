import streamlit as st
from sklearn import linear_model
import pandas as pd 
import numpy as np

df = pd.read_csv("hargakainbatik.csv")

model_regresi_linier = linear_model.LinearRegression()
model_regresi_linier.fit(df[["ukuran"]], df.harga)

st.title('prediksi harga kain batik')
ukuran  = st.number_input("masukkan ukuran kain", 0)

if st.button ("cek harga") :
    hasil = int(model_regresi_linier.predict([[ukuran]]))
    st.success(f"prediksi harga kain batik = Rp.{hasil}")