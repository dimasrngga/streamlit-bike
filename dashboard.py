import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

## title
st.title("Bike Sharing Data Analysis")

## header 1
st.header("Bagaimana pengaruh di weekdays dan weekend pada peminjaman sepeda?")

## data
all_data = pd.read_csv("all_data.csv")

## grafik
fig, ax = plt.subplots(figsize=(10,5))
sns.pointplot(data=all_data, x='hour', y='count', hue='weekday',ax=ax)
ax.set(title='count of bikes during weekdays and weekends')

st.pyplot(fig)


## header 2
st.header("bagaimana pengaruh cuaca terhadap peminjaman sepeda?")

## grafik
fig, ax = plt.subplots(figsize=(10,5))
sns.pointplot(data=all_data, x='hour', y='count', hue='weather',ax=ax)
ax.set(title='count of bikes during different weathers')

st.pyplot(fig)

## header kesimpulan 
st.header("Kesimpulan")

st.subheader("1.Bagaimana pengaruh di weekdays dan weekend pada peminjaman sepeda?")
st.text(F"Terdapat perbedaan garis pada pola pinjaman antara hari kerja dan akhir pekan.\npeminjaman pada hari kerja cenderung tinggi pada jam-jam sibuk pagi dan sore,\nsementara akhir pekan memiliki pola yang lebih rendah sepanjang hari")

st.subheader("2.bagaimana pengaruh cuaca terhadap peminjaman sepeda?")
st.text("cuaca memliki dampak yang lumayan signifikan pada peminjaman sepeda.\nseperti grafik di atas, peminjaman sepeda cenderung lebih tinggi pada warna biru\nmenadakan suhu yang nyaman dan sedikit berawan atau tidak ada hujan")
