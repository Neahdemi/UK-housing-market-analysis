import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Streamlit App
st.title('UK Housing Market Analysis')

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    house_prices = pd.read_csv(uploaded_file)
    
    # Convert "Date" column to datetime format
    house_prices["Date"] = pd.to_datetime(house_prices["Date"], format="%Y-%m")
    
    st.write("### Data Preview:")
    st.write(house_prices.head())

    # Quick price trend visualization
    st.write("### Price Trend Over Time:")
    plt.figure(figsize=(10,5))
    sns.lineplot(data=house_prices, x='Date', y='Average_Price')
    plt.title('UK House Prices Over Time')
    plt.xticks(rotation=45)
    st.pyplot(plt)

