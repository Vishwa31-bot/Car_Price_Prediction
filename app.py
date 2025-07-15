
import streamlit as st
import pandas as pd

st.title("🚗 Car Price Estimator (INR)")
st.write("A simple car price prediction app without machine learning.")

@st.cache_data
def load_data():
    return pd.read_csv("car_data_inr.csv")

df = load_data()
st.write("### Sample Data")
st.dataframe(df.head())

# Average base prices per brand (in INR)
avg_prices = df.groupby('brand')['price'].mean().to_dict()

st.write("### Estimate Your Car Price")

brand = st.selectbox("Brand", sorted(df['brand'].unique()))
model_type = st.selectbox("Model", sorted(df['model'].unique()))
year = st.slider("Year", int(df['year'].min()), int(df['year'].max()), 2018)
mileage = st.slider("Mileage (in km)", int(df['mileage'].min()), int(df['mileage'].max()), 50000)

# Basic depreciation and mileage penalty logic
current_year = 2025
age = current_year - year
base_price = avg_prices.get(brand, 1000000)
depreciation_factor = max(0.5, 1 - (age * 0.05))
mileage_penalty = mileage * 2  # INR per km
estimated_price = int(base_price * depreciation_factor - mileage_penalty)
estimated_price = max(estimated_price, 50000)  # minimum floor price

st.write(f"### Estimated Car Price: ₹{estimated_price:,.0f}")
