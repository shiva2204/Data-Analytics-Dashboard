import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Quick Analytics", layout="wide")
st.title("📈 Instant Data Analytics Dashboard")
st.markdown("Upload a CSV file to get started.")

# 2. File Uploader
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read Data
    df = pd.read_csv(uploaded_file)
    
    # 3. Data Overview Section
    st.subheader("📋 Data Preview")
    st.dataframe(df.head())
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔍 Basic Statistics")
        st.write(df.describe())
        
    with col2:
        st.subheader("🗂 Column Info")
        st.write(df.dtypes)

    st.divider()

    # 4. Visualization Section
    st.subheader("📊 Dynamic Visualizer")
    
    # Get numeric and categorical columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()

    chart_type = st.selectbox("Select Chart Type", ["Histogram", "Scatter Plot", "Box Plot"])

    if chart_type == "Histogram":
        target = st.selectbox("Select Column", numeric_cols)
        fig = px.histogram(df, x=target, nbins=30, title=f"Distribution of {target}")
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Scatter Plot":
        x_axis = st.selectbox("X Axis", numeric_cols)
        y_axis = st.selectbox("Y Axis", numeric_cols)
        color_by = st.selectbox("Color By (Categorical)", [None] + cat_cols)
        fig = px.scatter(df, x=x_axis, y=y_axis, color=color_by, title=f"{x_axis} vs {y_axis}")
        st.plotly_chart(fig, use_container_width=True)
    
    elif chart_type == "Box Plot":
        y_val = st.selectbox("Select Metric", numeric_cols)
        x_val = st.selectbox("Group By", cat_cols)
        fig = px.box(df, x=x_val, y=y_val, title=f"{y_val} by {x_val}")
        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("👆 Please upload a CSV file in the sidebar to begin.")
