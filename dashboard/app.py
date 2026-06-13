import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="Customer Churn Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("data/processed/cleaned_telco_churn.csv")

# Title
st.title("📊 Customer Churn Analytics Dashboard")

st.markdown(
    "Analyze customer churn patterns and key business metrics."
)

# =========================
# KPI METRICS
# =========================

total_customers = len(df)

churned_customers = len(
    df[df["Churn"] == "Yes"]
)

churn_rate = (
    churned_customers / total_customers
) * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Customers",
        total_customers
    )

with col2:
    st.metric(
        "Churned Customers",
        churned_customers
    )

with col3:
    st.metric(
        "Churn Rate (%)",
        f"{churn_rate:.2f}"
    )

st.divider()

# =========================
# CHURN DISTRIBUTION
# =========================

st.subheader("Customer Churn Distribution")

fig, ax = plt.subplots(figsize=(8, 5))

sns.countplot(
    x="Churn",
    data=df,
    ax=ax
)

plt.title("Customer Churn Distribution")

st.pyplot(fig)

# =========================
# CONTRACT TYPE ANALYSIS
# =========================

st.subheader("Contract Type Analysis")

fig, ax = plt.subplots(figsize=(8, 5))

sns.countplot(
    x="Contract",
    hue="Churn",
    data=df,
    ax=ax
)

plt.title("Contract Type vs Churn")

st.pyplot(fig)
# =========================
# TENURE ANALYSIS
# =========================

st.subheader("Tenure Distribution")

fig, ax = plt.subplots(figsize=(10, 5))

sns.histplot(
    data=df,
    x="tenure",
    hue="Churn",
    bins=30,
    ax=ax
)

plt.title("Tenure Distribution by Churn")

st.pyplot(fig)
# =========================
# MONTHLY CHARGES ANALYSIS
# =========================

st.subheader("Monthly Charges Analysis")

fig, ax = plt.subplots(figsize=(8, 5))

sns.boxplot(
    x="Churn",
    y="MonthlyCharges",
    data=df,
    ax=ax
)

plt.title("Monthly Charges by Churn")

st.pyplot(fig)

# =========================
# DATASET PREVIEW
# =========================

st.subheader("Dataset Preview")

st.dataframe(df.head())