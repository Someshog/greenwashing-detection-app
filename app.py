import streamlit as st
from transformers import pipeline
import torch
import time

# Set page config
st.set_page_config(
    page_title="Greenwashing Detection App",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 2rem;
    }
    .subheader {
        font-size: 1.5rem;
        color: #228B22;
        margin-bottom: 1rem;
    }
    .result-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .genuine {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .greenwashing {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .marketing-hype {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
    }
    .certification {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    .health-focused {
        background-color: #e2e3f3;
        border: 1px solid #d1d4e9;
        color: #383d41;
    }
    .confidence-bar {
        height: 20px;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'classifier' not in st.session_state:
    st.session_state.classifier = None
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False

@st.cache_resource
def load_model():
    """Load the zero-shot classification model"""
    try:
        classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=0 if torch.cuda.is_available() else -1
        )
        return classifier
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def analyze_claim(text, classifier):
    """Analyze sustainability claim for greenwashing"""
    candidate_labels = [
        "Greenwashing",
        "Genuine Sustainability",
        "Marketing Hype",
        "Certification-Based Claim",
        "Nutritional Health Focused"
    ]
    
    # Add more detailed labels for better classification
    detailed_labels = [
        "Misleading environmental claim",
        "Vague sustainability statement", 
        "Unsubstantiated green marketing",
        "Authentic environmental commitment",
        "Verified sustainable practice",
        "Transparent sustainability effort"
    ]
    
    try:
        # Primary classification
        result = classifier(text, candidate_labels)
        
        # Detailed analysis
        detailed_result = classifier(text, detailed_labels)
        
        return result, detailed_result
    except Exception as e:
        st.error(f"Error during classification: {str(e)}")
        return None, None

def display_results(result, detailed_result, text):
    """Display classification results"""
    if result is None:
        return
    
    # Main result
    prediction = result['labels'][0]
    confidence = result['scores'][0]
    
    # Determine styling based on prediction
    if prediction == "Greenwashing":
        result_class = "greenwashing"
        icon = "⚠️"
        color = "#dc3545"
    elif prediction == "Genuine Sustainability":
        result_class = "genuine"
        icon = "✅"
        color = "#28a745"
    elif prediction == "Marketing Hype":
        result_class = "marketing-hype"
        icon = "📢"
        color = "#ffc107"
    elif prediction == "Certification-Based Claim":
        result_class = "certification"
        icon = "🏆"
        color = "#17a2b8"
    elif prediction == "Nutritional Health Focused":
        result_class = "health-focused"
        icon = "🥗"
        color = "#6f42c1"
    else:
        result_class = "genuine"
        icon = "❓"
        color = "#6c757d"
    
    # Display main result
    st.markdown(f"""
    <div class="result-box {result_class}">
        <h3>{icon} Classification Result</h3>
        <p><strong>Prediction:</strong> {prediction}</p>
        <p><strong>Confidence:</strong> {confidence:.2%}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Confidence visualization
    st.subheader("Confidence Scores")
    for label, score in zip(result['labels'], result['scores']):
        st.metric(label, f"{score:.2%}")
        st.progress(score)
    
    # Detailed analysis
    if detailed_result:
        st.subheader("Detailed Analysis")
        
        # Group detailed results
        problematic_indicators = []
        positive_indicators = []
        
        for label, score in zip(detailed_result['labels'], detailed_result['scores']):
            if any(keyword in label.lower() for keyword in ['misleading', 'vague', 'unsubstantiated']):
                problematic_indicators.append((label, score))
            else:
                positive_indicators.append((label, score))
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Problematic Indicators:**")
            for label, score in problematic_indicators:
                st.write(f"• {label}: {score:.2%}")
        
        with col2:
            st.markdown("**Positive Indicators:**")
            for label, score in positive_indicators:
                st.write(f"• {label}: {score:.2%}")

def main():
    # Header
    st.markdown('<h1 class="main-header">🌱 Greenwashing Detection App</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    This app uses AI-powered zero-shot classification to detect potential greenwashing in sustainability claims.
    Enter a sustainability claim below to analyze its authenticity.
    """)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## About")
        st.markdown("""
        **Greenwashing** refers to misleading claims about environmental benefits.
        
        This app uses the `facebook/bart-large-mnli` model to classify sustainability claims into:
        - ⚠️ **Greenwashing**: Misleading or unsubstantiated claims
        - ✅ **Genuine Sustainability**: Authentic environmental commitments
        - 📢 **Marketing Hype**: Promotional language without substance
        - 🏆 **Certification-Based Claim**: Claims backed by certifications
        - 🥗 **Nutritional Health Focused**: Health-oriented sustainability claims
        """)
        
        st.markdown("## How it works")
        st.markdown("""
        1. Enter a sustainability claim
        2. AI analyzes the text using zero-shot classification
        3. Get results with confidence scores
        4. View detailed analysis breakdown
        """)
        
        # Model info
        st.markdown("## Model Information")
        st.markdown("""
        - **Model**: facebook/bart-large-mnli
        - **Type**: Zero-shot classification
        - **Framework**: Hugging Face Transformers
        """)
    
    # Load model
    if not st.session_state.model_loaded:
        with st.spinner("Loading AI model... This may take a moment."):
            st.session_state.classifier = load_model()
            if st.session_state.classifier:
                st.session_state.model_loaded = True
                st.success("Model loaded successfully!")
            else:
                st.error("Failed to load model. Please try again.")
                return
    
    # Main interface
    st.markdown('<h2 class="subheader">Analyze Sustainability Claim</h2>', unsafe_allow_html=True)
    
    # Text input
    claim_text = st.text_area(
        "Enter a sustainability claim to analyze:",
        height=100,
        placeholder="e.g., 'Our product is made from 100% recycled materials and is carbon neutral.'"
    )
    
    # Example claims
    st.markdown("**Example claims to try:**")
    examples = [
        "Our product is eco-friendly and good for the environment.",
        "We use 100% certified organic cotton sourced from fair-trade farms with verified supply chain transparency.",
        "This amazing natural product will revolutionize your life!",
        "Certified by USDA Organic and Fair Trade USA with traceable supply chain documentation.",
        "Our vitamin-enriched sustainable formula promotes both environmental and personal health."
    ]
    
    selected_example = st.selectbox("Or select an example:", [""] + examples)
    if selected_example:
        claim_text = selected_example
    
    # Analysis button
    if st.button("Analyze Claim", type="primary"):
        if claim_text.strip():
            if st.session_state.classifier:
                with st.spinner("Analyzing claim..."):
                    result, detailed_result = analyze_claim(claim_text, st.session_state.classifier)
                    
                if result:
                    display_results(result, detailed_result, claim_text)
                    
                    # Additional insights
                    st.markdown("---")
                    st.markdown("### 💡 Tips for Identifying Greenwashing")
                    st.markdown("""
                    - Look for **vague terms** like "eco-friendly" or "natural" without specific details
                    - Check for **third-party certifications** and verified claims
                    - Be wary of **unsubstantiated superlatives** like "100% green"
                    - Look for **transparency** in supply chain and manufacturing processes
                    """)
            else:
                st.error("Model not loaded. Please refresh the page.")
        else:
            st.warning("Please enter a sustainability claim to analyze.")
    
    # Future features section
    st.markdown("---")
    st.markdown("### 🚀 Coming Soon")
    st.markdown("""
    - **Product Ingredients Analysis**: Upload ingredient lists for sustainability assessment
    - **Batch Analysis**: Analyze multiple claims at once
    - **Company Sustainability Reports**: Analyze entire sustainability reports
    - **Historical Tracking**: Track changes in sustainability claims over time
    """)
    
    # Ingredients analysis placeholder (for future implementation)
    with st.expander("🧪 Product Ingredients Analysis (Coming Soon)"):
        st.markdown("This feature will allow you to analyze product ingredients for sustainability claims.")
        ingredients_text = st.text_area(
            "Enter product ingredients (feature under development):",
            height=80,
            placeholder="e.g., Water, Organic Aloe Vera, Sustainable Palm Oil...",
            disabled=True
        )
        st.button("Analyze Ingredients", disabled=True)

if __name__ == "__main__":
    main()
