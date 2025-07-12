# 🌱 Spot the Greenwash: Sustainability Claim Analyzer

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-green?style=flat-square) ![Model](https://img.shields.io/badge/Model-DistilBERT%20MNLI-blue?style=flat-square)

## Overview

Spot the Greenwash is an AI-powered Streamlit app that helps you analyze sustainability claims and spot greenwashing in product marketing. Using advanced Natural Language Processing (NLP) and zero-shot classification, the app empowers consumers to make informed, environmentally conscious decisions and hold brands accountable for their claims.

---

## 🚀 Features
- **Zero-shot claim classification**: Detect Greenwashing, Genuine Sustainability, and Marketing Hype
- **Confidence scores**: Visualize how strongly a claim matches each category
- **Detailed indicator analysis**: See top indicators for each category
- **Example claims**: Try the app with built-in sample claims
- **Beautiful UI**: Modern, clean, and easy to use
- **About Us section**: Learn about the mission and team
- **Future roadmap**: Batch analysis, ingredient analysis, report uploads, and more

---

## 🧠 AI Model
- **Model Used**: [`joeddav/distilbert-base-uncased-mnli`](https://huggingface.co/joeddav/distilbert-base-uncased-mnli)
- **Method**: Zero-shot classification via Hugging Face Transformers
- **Categories**:
  - Greenwashing
  - Genuine Sustainability
  - Marketing Hype
- **Indicators**: Each category has detailed sub-labels for deeper analysis

---

## 💻 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/greenwashing-detection-app.git
   cd greenwashing-detection-app
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deploy on Streamlit Cloud
- Push your code to GitHub
- Go to [Streamlit Cloud](https://streamlit.io/cloud)
- Create a new app, select your repo and `app.py`
- Your app will be live and shareable!

---

## 🖼️ Screenshots
Add screenshots of your app in `SCREENSHOTS.md` to showcase the UI and features.

---

## 📋 Example Claims
- "Our product is eco-friendly and good for the environment."
- "We use 100% certified organic cotton sourced from fair-trade farms with verified supply chain transparency."
- "This amazing natural product will revolutionize your life!"
- "Our revolutionary green technology reduces carbon emissions without any compromise on performance."
- "Made with sustainable materials that protect the planet for future generations."

---

## 🏆 Why This App Stands Out
- **Real-time AI analysis**: Instantly spot misleading claims
- **User-friendly**: No technical expertise required
- **Open-source**: Transparent and extensible
- **Social impact**: Empowers consumers and promotes honest sustainability

---

## 👥 Team & Mission
**Built by Team BharatWin**

**Our Mission:**
> To democratize access to sustainability information and empower consumers to make informed, environmentally conscious purchasing decisions while holding brands accountable for their environmental claims.

**Contact:** info@greenwashapp.com

---

## 📄 License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🙌 Contributing
We welcome contributions! See `CONTRIBUTING.md` for guidelines.

---

## 💡 Future Roadmap
- Product ingredient analysis
- Batch claim analysis
- Sustainability report uploads
- Historical tracking of claims

---

## ⭐ If you like this project, star it on GitHub and share with others!
