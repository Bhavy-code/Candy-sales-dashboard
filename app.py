import streamlit as st
import pandas as pd

# Page Settings
st.set_page_config(
    page_title="Nassau Candy Dashboard",
    page_icon="🍫",
    layout="wide"
)

# Title
st.title("🍫 Nassau Candy Sales Dashboard")
st.markdown("### Sales Performance Analysis")

# Load Data
df = pd.read_csv("data.csv", encoding="utf-8")

# Sidebar Filter
st.sidebar.header("Filters")

region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].dropna().unique())
)

if region != "All":
    df = df[df["Region"] == region]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Sales", f"${df['Sales'].sum():,.2f}")

with col2:
    st.metric("Total Profit", f"${df['Gross Profit'].sum():,.2f}")

with col3:
    st.metric("Total Units", int(df["Units"].sum()))

with col4:
    st.metric("Total Cost", f"${df['Cost'].sum():,.2f}")

st.divider()

# Dataset Preview
st.subheader("📋 Dataset Preview")
st.dataframe(df.head())

# Download Button
st.download_button(
    label="📥 Download Dataset",
    data=df.to_csv(index=False),
    file_name="sales_data.csv",
    mime="text/csv"
)

# Sales by Region
st.subheader("🌍 Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)

# Sales by Division
st.subheader("🏢 Sales by Division")
division_sales = df.groupby("Division")["Sales"].sum()
st.bar_chart(division_sales)

# Sales by State
st.subheader("🗺️ Sales by State")
state_sales = (
    df.groupby("State/Province")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
st.bar_chart(state_sales)

# Top Products
st.subheader("📦 Top 10 Products")
product_sales = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
st.bar_chart(product_sales)

# Top Cities
st.subheader("🏙️ Top 10 Cities by Sales")
city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
st.bar_chart(city_sales)

# Statistics
st.subheader("📊 Dataset Statistics")
st.dataframe(df.describe())

# Footer
st.markdown("---")
st.markdown(
    """
    ### 📊 Nassau Candy Sales Dashboard
    Built with Streamlit & Python
    """
)