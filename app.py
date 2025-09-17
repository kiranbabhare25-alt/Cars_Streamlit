import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("CARS.csv")

# Streamlit App Title
st.title("Car Horsepower by Model")

# Display the first few rows
st.subheader("Preview of Dataset")
st.dataframe(df.head(2))

# Unique car brands
brands = df['Make'].unique()

# User selects a brand
c = st.selectbox("Select a Brand", options=brands)

# Filter data based on selected brand
s = df[df.Make == c]

# Check if there are models to display
if not s.empty:
    st.subheader(f"Horsepower of {c} Models")

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    sb.barplot(x=s.Model, y=s.Horsepower, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)
else:
    st.warning("No models found for the selected brand.")
