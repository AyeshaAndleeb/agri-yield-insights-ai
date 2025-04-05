import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from groq import Groq

# Page config
st.set_page_config(
    page_title="🌾 Agri Insights Dashboard",
    layout="wide",
    page_icon="🌿"
)

# Custom CSS for cleaner UI
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fa;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 2rem;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 0.6em 1.5em;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Groq
client = Groq(api_key="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")

# Title
st.markdown('<div class="title">🌾 Agricultural Yield Insights Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload your dataset and get expert insights powered by LLaMA-3 ✨</div>', unsafe_allow_html=True)

# Upload Section
st.markdown("### 📂 Upload Your Agricultural Data (CSV)")
uploaded_file = st.file_uploader("", type=["csv"])

# Process file
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Show Data
    with st.container():
        st.markdown("### 🔍 Data Preview")
        st.dataframe(df.head(), use_container_width=True)

    # Select ID
    id_list = df["ID"].unique().tolist()
    land_id = st.selectbox("🔢 Select Land ID for Analysis", id_list)

    # Submit button
    if st.button("🚀 Generate Insights"):
        with st.spinner("Analyzing data..."):
            def generate_insights(df, land_id):
                if "ID" not in df.columns:
                    return "❌ **Error:** The dataset must contain an 'ID' column.", None

                land_data = df[df["ID"] == land_id]
                if land_data.empty:
                    return f"⚠️ **No data found for ID:** `{land_id}`", None

                land_info = land_data.to_dict(orient="records")[0]

                prompt = f"""
                Given the following agricultural data, provide insights about soil quality, seed variety, 
                fertilizer amount, and expected yield:

                {land_info}
                """

                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                )

                return chat_completion.choices[0].message.content, land_info

            insights, land_info = generate_insights(df, land_id)

        if land_info:
            st.markdown("### 📄 AI-Generated Insights")
            st.success(insights)

            # Comparison Plots
            st.markdown("### 📊 Comparative Visualizations")
            def plot_comparisons(df, land_id):
                land_data = df[df["ID"] == land_id]
                if land_data.empty:
                    st.warning("⚠️ No data available for selected ID.")
                    return

                fig, axes = plt.subplots(1, 3, figsize=(18, 5))

                sns.set_style("whitegrid")

                # Fertilizer
                sns.boxplot(x="Fertilizer_Amount_kg_per_hectare", data=df, ax=axes[0], color="lightgreen")
                axes[0].axvline(land_data["Fertilizer_Amount_kg_per_hectare"].values[0], color="red", linestyle="--")
                axes[0].set_title("Fertilizer Amount (kg/hectare)", fontsize=12)

                # Sunny Days
                sns.boxplot(x="Sunny_Days", data=df, ax=axes[1], color="gold")
                axes[1].axvline(land_data["Sunny_Days"].values[0], color="red", linestyle="--")
                axes[1].set_title("Sunny Days", fontsize=12)

                # Rainfall
                sns.boxplot(x="Rainfall_mm", data=df, ax=axes[2], color="skyblue")
                axes[2].axvline(land_data["Rainfall_mm"].values[0], color="red", linestyle="--")
                axes[2].set_title("Rainfall (mm)", fontsize=12)

                st.pyplot(fig)

            plot_comparisons(df, land_id)

else:
    st.info("👈 Please upload a CSV file to begin.")
