# 🌾 Agri Yield Insights AI

A visually appealing AI-powered web application that generates smart agricultural insights based on uploaded CSV datasets. This app uses **Groq's LLaMA-3-70B** model for intelligent analysis and provides stunning comparative visualizations using `matplotlib` and `seaborn`.

---

## 🚀 Live Demo (Hugging Face Space)

👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/Ayesha003/AgriConnectInsights)

---

## 📸 Features

- 📂 Upload agricultural datasets (CSV format)
- 🧠 Get smart insights using **LLaMA-3** via **Groq API**
- 📊 Interactive visual comparisons:
  - Fertilizer usage
  - Sunny days
  - Rainfall patterns
- 🌟 Beautiful, centered, and responsive UI with custom styles
- 📱 Runs seamlessly on both desktop and mobile devices

---

## 🛠️ Tech Stack

- **Frontend & UI**: Streamlit
- **Data Handling**: Pandas
- **Visualizations**: Matplotlib, Seaborn
- **AI Integration**: Groq API using LLaMA-3
- **Deployment**: Hugging Face Spaces

---

## 🧪 Dataset Requirements

Your CSV file must include the following columns:

| Column Name                        | Description                            |
|-----------------------------------|----------------------------------------|
| `ID`                              | Unique identifier for each land plot   |
| `Fertilizer_Amount_kg_per_hectare`| Amount of fertilizer used              |
| `Sunny_Days`                      | Number of sunny days                   |
| `Rainfall_mm`                     | Rainfall in millimeters                |

✅ **Example row**:

```csv
ID,Fertilizer_Amount_kg_per_hectare,Sunny_Days,Rainfall_mm
A01,60,28,340
