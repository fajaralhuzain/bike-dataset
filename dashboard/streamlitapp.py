import os
import streamlit as st
import pandas as pd
import plotly.express as px

# # Load dataset
# file_path = "day.csv"
file_path = os.path.join(os.path.dirname(__file__), "day.csv")
df = pd.read_csv(file_path)

# Convert dteday to datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Title
st.title("Dashboard Analisis Data Penyewaan Sepeda")

# Sidebar
st.sidebar.header("Filter Data")
selected_month = st.sidebar.selectbox("Pilih Bulan", df['mnth'].unique())
filtered_df = df[df['mnth'] == selected_month]

# RFM Analysis
st.header("RFM Analysis")
filtered_df['Recency'] = (df['dteday'].max() - df['dteday']).dt.days
filtered_df['Frequency'] = df['cnt']
filtered_df['Monetary'] = df['cnt']
st.dataframe(filtered_df[['Recency', 'Frequency', 'Monetary']])

# RFM Bar Chart Visualization
st.subheader("Visualisasi RFM Analysis")
fig_rfm = px.bar(filtered_df, x='dteday', y='cnt', title='Jumlah Penyewaan Sepeda per Hari')
st.plotly_chart(fig_rfm)

# Clustering tanpa ML (Kategori berdasarkan aturan)
st.header("Clustering Penyewaan")
def categorize_rentals(cnt):
    if cnt < 1000:
        return "Low"
    elif cnt < 3000:
        return "Medium"
    else:
        return "High"
filtered_df['Cluster'] = filtered_df['cnt'].apply(categorize_rentals)
st.bar_chart(filtered_df.groupby('Cluster').size())

# Geospatial Analysis (Jika ada data lokasi, bisa ditambahkan di sini)

st.write("Tidak menampilkan data geospasial dikarenakan didalam data csv tersebut tidak ada data wilayah")