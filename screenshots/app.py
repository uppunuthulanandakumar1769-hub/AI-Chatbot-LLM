import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="AI Supply Chain Forecasting Platform",
    page_icon="📦",
    layout="wide"
)
st.title(" AI-Powered Supply Chain Forecasting Platform")

st.markdown("
#Intelligent Analytics Dashboard for:
- Demand Forecasting
- Inventory Optimization
- Supplier Analytics
- Business Intelligence
- Predictive Analytics")
np.random.seed(42)
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"]
products = [
    "Product A",
    "Product B",
    "Product C",
    "Product D",
    "Product E"]
suppliers = [
    "Supplier X",
    "Supplier Y",
    "Supplier Z"]
data = pd.DataFrame({
    "Month": np.random.choice(months, 300),
    "Product": np.random.choice(products, 300),
    "Supplier": np.random.choice(suppliers, 300),
    "Sales": np.random.randint(100, 1000, 300),
    "Inventory": np.random.randint(50, 500, 300),
    "Forecast Demand": np.random.randint(150, 1200, 300),
    "Supplier Score": np.random.uniform(60, 100, 300).round(2)})
st.sidebar.header("Dashboard Filters")
selected_product = st.sidebar.selectbox(
    "Select Product",
    ["All"] + products)
selected_month = st.sidebar.selectbox(
    "Select Month",
    ["All"] + months)
filtered_data = data.copy()
if selected_product != "All":
    filtered_data = filtered_data[
        filtered_data["Product"] == selected_product]
if selected_month != "All":
    filtered_data = filtered_data[
        filtered_data["Month"] == selected_month]
total_sales = filtered_data["Sales"].sum()
average_inventory = int(
    filtered_data["Inventory"].mean())
forecast_total = filtered_data[
    "Forecast Demand"].sum()
col1, col2, col3 = st.columns(3)
col1.metric(
    " Total Sales",
    f"${total_sales:,}")
col2.metric(
    "Average Inventory",
    f"{average_inventory}")
col3.metric(
    " Forecast Demand",
    f"{forecast_total:,}")
st.subheader(" Monthly Sales Analytics")
sales_chart = px.bar(
    filtered_data,
    x="Month",
    y="Sales",
    color="Product",
    barmode="group",
    title="Monthly Sales Distribution")
st.plotly_chart(
    sales_chart,
    use_container_width=True)
st.subheader(" Inventory Distribution")
inventory_chart = px.pie(
    filtered_data,
    names="Product",
    values="Inventory",
    title="Inventory Share by Product")
st.plotly_chart(
    inventory_chart,
    use_container_width=True)
st.subheader("AI Demand Forecasting")
forecast_chart = px.line(
    filtered_data,
    x="Month",
    y="Forecast Demand",
    color="Product",
    markers=True,
    title="Predicted Demand Trends")
st.plotly_chart(
    forecast_chart,
    use_container_width=True)
st.subheader(" Supplier Performance Analytics")
supplier_summary = (
    filtered_data.groupby("Supplier")
        ["Supplier Score"]
    .mean()
    .reset_index())
supplier_chart = px.bar(
    supplier_summary,
    x="Supplier",
    y="Supplier Score",
    color="Supplier Score",
    title="Supplier Performance Score")
st.plotly_chart(supplier_chart,use_container_width=True)
st.subheader("Supply Chain Dataset")
st.dataframe(filtered_data,use_container_width=True)
st.subheader("AI Insights")
top_product = (
    filtered_data.groupby("Product")["Sales"]
    .sum()
    .idxmax()
)
st.success(f"Top Performing Product: {top_product}")
low_inventory = filtered_data[filtered_data["Inventory"] < 100]
st.warning(f"{len(low_inventory)} low inventory records detected.")
st.markdown("  ")
st.markdown("
 Technologies Used
- Streamlit
- Pandas
- NumPy
- Plotly
- Predictive Analytics
Developed by U. Nanda Kumar
")
