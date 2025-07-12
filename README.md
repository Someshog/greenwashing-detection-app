git_setup.bat# Greenwashing Detection App 🌱

A Streamlit web application that uses AI-powered zero-shot classification to detect potential greenwashing in sustainability claims.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub stars](https://img.shields.io/github/stars/yourusername/greenwashing-detection-app?style=social)

## 🚀 Features

- **AI-Powered Analysis**: Uses Facebook's BART-large-mnli model for zero-shot classification
- **5-Category Classification**: 
  - ⚠️ **Greenwashing**: Misleading claims
  - ✅ **Genuine Sustainability**: Authentic commitments  
  - 📢 **Marketing Hype**: Promotional language
  - 🏆 **Certification-Based**: Backed by certifications
  - 🥗 **Health Focused**: Nutritional sustainability claims
- **Real-time Analysis**: Instant results with confidence scores
- **Modern UI**: Clean interface with visual indicators

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example Claims](#example-claims)
- [Model Information](#model-information)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/greenwashing-detection-app.git
   cd greenwashing-detection-app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

### Running the App

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your web browser** and go to `http://localhost:8501`

3. **Analyze claims**:
   - Enter a sustainability claim in the text area
   - Or select from example claims
   - Click "Analyze Claim" to get results

### Command Line Demo

Run the demo script to see the core functionality:
```bash
python demo.py
```

### Testing Setup

Verify your installation:
```bash
python test_setup.py
```

## 🔬 How It Works

The app uses Hugging Face's `facebook/bart-large-mnli` model for zero-shot classification:

1. **Input Processing**: Takes user input (sustainability claim)
2. **AI Analysis**: Classifies the claim using zero-shot classification
3. **Multi-label Classification**: Assigns claims to one of 5 categories
4. **Confidence Scoring**: Provides confidence scores for each category
5. **Detailed Analysis**: Shows breakdown of problematic vs. positive indicators
6. **Visual Results**: Displays results with color-coded indicators

## 📊 Example Claims

Try these examples to see how the app works:

### Potential Greenwashing
- "Our product is eco-friendly and good for the environment."
- "This item is natural and green."

### Marketing Hype
- "This amazing natural product will revolutionize your life!"

### Genuine Sustainability
- "We use 100% certified organic cotton sourced from fair-trade farms with verified supply chain transparency."
- "Our manufacturing process is powered by 100% renewable energy with third-party verified carbon offsets."

### Certification-Based Claims
- "Certified by USDA Organic and Fair Trade USA with traceable supply chain documentation."

### Nutritional Health Focused
- "Our vitamin-enriched sustainable formula promotes both environmental and personal health."

## 🤖 Model Information

- **Model**: `facebook/bart-large-mnli`
- **Type**: Zero-shot classification
- **Framework**: Hugging Face Transformers
- **Task**: Natural Language Inference (NLI)
- **Size**: ~1.6GB (downloaded automatically on first run)
- **GPU Support**: Automatic GPU acceleration if available

## 📸 Screenshots

### Main Interface
The clean, modern interface with sustainability claim analysis.

### Results Display
Color-coded results with confidence scores and detailed analysis.

### Example Claims
Pre-loaded examples for testing different types of claims.

## 🗂️ Project Structure

```
greenwashing-detection-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── demo.py               # Command-line demo
├── test_setup.py         # Installation verification
├── .gitignore            # Git ignore file
├── LICENSE               # MIT License
└── screenshots/          # App screenshots (add your own)
```

## 🚀 Future Features

- **Product Ingredients Analysis**: Upload ingredient lists for sustainability assessment
- **Batch Analysis**: Analyze multiple claims at once
- **Company Sustainability Reports**: Analyze entire sustainability reports
- **Historical Tracking**: Track changes in sustainability claims over time
- **API Integration**: REST API for programmatic access
- **Export Results**: Download analysis results as PDF/CSV

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hugging Face** for the transformers library and pre-trained models
- **Facebook AI** for the BART-large-mnli model
- **Streamlit** for the awesome web app framework
- **OpenAI** for inspiration on sustainability and AI applications

## 📧 Contact

- **Project Link**: [https://github.com/yourusername/greenwashing-detection-app](https://github.com/yourusername/greenwashing-detection-app)
- **Issues**: [https://github.com/yourusername/greenwashing-detection-app/issues](https://github.com/yourusername/greenwashing-detection-app/issues)

## ⚠️ Disclaimer

This tool is for educational and research purposes. While it uses state-of-the-art AI models, the classifications should not be considered as definitive legal or regulatory assessments. Always consult with sustainability experts and regulatory guidelines for official evaluations.

---

Made with ❤️ and 🤖 AI
