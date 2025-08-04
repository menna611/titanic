import streamlit as st
import pandas as pd
import plotly.express as px

# Load Titanic data
df = pd.read_csv('C:\\Users\\Incorta\\Desktop\\m\\train.csv')


# Title
st.title("Titanic Survival Prediction")

# Dropdown for Passenger Class
passenger_class = st.selectbox("Select Passenger Class", [1, 2, 3])

# Filter data based on class
filtered_df = df[df['Pclass'] == passenger_class]

# Plot survival rate
fig = px.histogram(filtered_df, x='Age', color='Survived', title=f'Survival Rate for Class {passenger_class}')
st.plotly_chart(fig)

# Display basic data table
st.write(filtered_df.head())

