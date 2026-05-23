import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="Sales Data Analysis Dashboard",
    layout="wide"
)

# Title
st.title("📊 Sales Data Analysis Dashboard")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_sales_data.csv")
    return df

df = load_data()

# Show Dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Basic Information
st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Rows", df.shape[0])

with col2:
    st.metric("Total Columns", df.shape[1])

with col3:
    st.metric("Missing Values", df.isnull().sum().sum())

# Sidebar Filters
st.sidebar.header("Filter Data")

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

selected_column = st.sidebar.selectbox(
    "Select Numeric Column",
    numeric_cols
)

# Statistical Summary
st.subheader("Statistical Summary")
st.write(df.describe())

# Histogram
st.subheader(f"Distribution of {selected_column}")

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df[selected_column], kde=True, ax=ax)

st.pyplot(fig)

# Correlation Heatmap
st.subheader("Correlation Heatmap")

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap='coolwarm',
            ax=ax2)

st.pyplot(fig2)

# Top Values Analysis
st.subheader("Top Value Counts")

categorical_cols = df.select_dtypes(include=['object']).columns

if len(categorical_cols) > 0:
    selected_cat = st.selectbox(
        "Select Categorical Column",
        categorical_cols
    )

    top_values = df[selected_cat].value_counts().head(10)

    st.bar_chart(top_values)

# Insights Section
st.subheader("Business Insights")

st.markdown("""
- Identified top-performing categories/products
- Analyzed trends and customer behavior
- Explored correlations between numerical features
- Generated visual insights from sales data
""")

# Footer
st.markdown("---")
st.markdown("Developed by Zishan Baig 🚀")