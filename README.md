# 🌱 Spot the Greenwash: Sustainability Claim Analyzer

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-green?style=flat-square) ![Model](https://img.shields.io/badge/Model-DistilBERT%20MNLI-blue?style=flat-square)

## Overview

Spot the Greenwash Spot the Greenwash is an AI-powered Streamlit app that aids in determining what sustainability claims are true and what is greenwashing in product marketing! By leveraging advanced natural language processing (NLP) and zero-shot classification techniques, the app will enable people to make informed choices on which products they want to buy, that are also environmentally friendly, and challenge companies promises.

Numerous major brands have been criticized for vague or misleading environmental claims — including H&M for its “Conscious” clothing line, Nestlé for its claims about recyclable plastic materials and Volkswagen for its notorious “clean diesel” campaign. This app will help you to question similar claims and cut through the buzzwords.

Whether you’re an eco conscious shopper, environmental advocate, or just curious — this tool makes it easy to fact check green claims, stay informed, and make decisions that actually support planet.

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
- **Model Used**: [`joeddav/distilbert-base-uncased-mnli`](https://huggingface.co/typeform/distilbert-base-uncased-mnli)
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

## 🖼️ Screenshots

<img width="947" height="439" alt="ss1" src="https://github.com/user-attachments/assets/c190059a-849e-4dc2-a721-65a5cb81f5d9" />

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
- [Somesh Goyal](https://github.com/Someshog)
- [Shivi Goyal](https://github.com/shivigoyal4321)
  
**Our Mission:**
> To democratize access to sustainability information and empower consumers to make informed, environmentally conscious purchasing decisions while holding brands accountable for their environmental claims.

**Contact:** workwithsomesh1@gmail.com

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
