import streamlit as st
from transformers import pipeline
import torch
import time
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="Spot the Greenwash: Know What You're Buying",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-family: 'Playfair Display', serif !important;
        font-size: 2.5rem;
        color: #ffffff !important;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .tagline {
        font-family: 'Inter', sans-serif !important;
        font-size: 1.25rem;
        color: #ffffff;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 400;
        opacity: 0.9;
    }
    .subheader {
        font-size: 1.5rem;
        color: #228B22;
        margin-bottom: 1rem;
    }
    .section-box {
        background: none;
        backdrop-filter: blur(10px);
        border-radius: 20px;
        color: #ffffff;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        padding: 2rem;
        margin: 1rem auto;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .section-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
    }
    
    .section-title {
        font-family: 'Playfair Display', serif !important;
        color: #ffffff;
        font-size: 1.7rem;
        margin-bottom: 1rem;
        font-weight: 700;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 2px;
    }
    
    .section-text {
        font-family: 'Inter', sans-serif !important;
        font-size: 1.0rem;
        color: #ffffff;
        line-height: 1.7;
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

# Label mapping for main categories and their detailed indicators
label_map = {
    "Greenwashing": [
        "Misleading environmental claim",
        "Vague sustainability statement",
        "Unsubstantiated green marketing",
        "Overstated eco-friendly benefits",
        "Use of irrelevant green imagery"
    ],
    "Genuine Sustainability": [
        "Authentic environmental commitment",
        "Verified sustainable practice",
        "Third-party sustainability certification",
        "Transparency in environmental impact",
        "Evidence-based climate action"
    ],
    "Marketing Hype": [
        "Generic green buzzwords",
        "Emotional appeal without proof",
        "Sustainability used as a selling point",
        "Trendy environmental phrasing"
    ]
}

def analyze_claim(text, classifier):
    """Analyze sustainability claim for greenwashing"""
    candidate_labels = [
        "Greenwashing",
        "Genuine Sustainability",
        "Marketing Hype"
    ]
    # Use all detailed labels from label_map
    detailed_labels = []
    for labels in label_map.values():
        detailed_labels.extend(labels)
    try:
        # Primary classification
        result = classifier(text, candidate_labels, multi_label=True)
        # Detailed analysis
        detailed_result = classifier(text, detailed_labels, multi_label=True)
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

    # Big bold gauge chart for top prediction
    st.markdown("#### Main Classification Confidence")
    fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=confidence * 100,
    number={
        'suffix': " %",
        'font': {'size': 28, 'color': color}
    },
    title={
        'text': f"<b>{prediction}</b>",
        'font': {'size': 20}
    },
    gauge={
        'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#444"},
        'bar': {'color': color, 'thickness': 0.2},
        'bgcolor': "white",
        'borderwidth': 1,
        'bordercolor': "#ccc",
        'steps': [
            {'range': [0, 50], 'color': '#f2f2f2'},
            {'range': [50, 100], 'color': '#e6f4ea' if confidence >= 0.5 else '#fbeaea'}
        ],
        'threshold': {
            'line': {'color': color, 'width': 2},
            'thickness': 0.7,
            'value': confidence * 100
        },
    }
))

    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        height=250  # Reduce overall height
    )
        # Display
    st.plotly_chart(fig, use_container_width=True)
    
    # Confidence visualization
    st.subheader("Confidence Scores")
    for label, score in zip(result['labels'], result['scores']):
        st.metric(label, f"{score:.2%}")
        st.progress(score)
    

#         st.subheader("Detailed Analysis")
        
#         # Group detailed results by main category using label_map
#         grouped = {cat: [] for cat in label_map}
#         for label, score in zip(detailed_result['labels'], detailed_result['scores']):
#             for cat, labels in label_map.items():
#                 if label in labels:
#                     grouped[cat].append((label, score))
#                     break
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.markdown("**Greenwashing Indicators:**")
#             for label, score in grouped["Greenwashing"]:
#                 st.write(f"• {label}: {score:.2%}")
        
#         with col2:
#             st.markdown("**Genuine Sustainability Indicators:**")
#             for label, score in grouped["Genuine Sustainability"]:
#                 st.write(f"• {label}: {score:.2%}")
        
#         with col3:
#             st.markdown("**Marketing Hype Indicators:**")
#             for label, score in grouped["Marketing Hype"]:
#                 st.write(f"• {label}: {score:.2%}")
# Detailed analysis with improved layout
    if detailed_result:
        st.markdown("---")
        st.markdown("### 🔍 Detailed Indicator Analysis")
        
        # Group detailed results by main category
        grouped = {cat: [] for cat in label_map}
        for label, score in zip(detailed_result['labels'], detailed_result['scores']):
            for cat, labels in label_map.items():
                if label in labels:
                    grouped[cat].append((label, score))
                    break
        
        # Display in three columns with enhanced cards
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("**🚨 Greenwashing Indicators**")
            for label, score in grouped["Greenwashing"][:3]:  # Show top 3
                st.write(f"• {label}: {score:.1%}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("**✅ Genuine Sustainability Indicators**")
            for label, score in grouped["Genuine Sustainability"][:3]:  # Show top 3
                st.write(f"• {label}: {score:.1%}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.markdown("**📢 Marketing Hype Indicators**")
            for label, score in grouped["Marketing Hype"][:3]:  # Show top 3
                st.write(f"• {label}: {score:.1%}")
            st.markdown('</div>', unsafe_allow_html=True)
def main():
    # Header
    st.markdown('''
    <div style="max-width:900px;margin:2rem auto 0 auto;" class="fade-in-up">
        <h1 class="main-header">🌱 Spot the Greenwash</h1>
        <div class="tagline">AI-powered sustainability claim analysis • Know what you're really buying</div>
    </div>
    ''', unsafe_allow_html=True)    

    # Enhanced What is Greenwashing Section
    st.markdown('''
    <div class="section-box fade-in-up">
        <div class="section-title">What is Greenwashing?</div>
        <div class="section-text">
            Greenwashing is a deceptive marketing practice where companies use misleading environmental claims to appear more sustainable than they actually are. These false or exaggerated claims can include vague terms like "eco-friendly," unsubstantiated carbon neutral promises, or irrelevant certifications.
            <br><br>
            Our AI-powered tool helps you cut through the marketing noise and identify potentially misleading sustainability claims, empowering you to make truly informed purchasing decisions.
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 🎯 How It Works")
        st.markdown("""
        Our analysis uses advanced Natural Language Processing to classify sustainability claims:
        
        **🔴 Greenwashing**: Misleading, vague, or unsubstantiated environmental claims
        
        **🟢 Genuine Sustainability**: Authentic commitments with verifiable backing
        
        **🟡 Marketing Hype**: Promotional language that lacks substance
        """)
        
        st.markdown("---")
        st.markdown("## 🧠 AI Technology")
        st.markdown("""
        - **Model**: `Facebook BART-Large-MNLI`
        - **Method**: Zero-shot classification
        - **Analysis**: Multi-label confidence scoring
        - **Accuracy**: Trained on millions of text samples
        """)
        
        st.markdown("---")
        st.markdown("## 📊 Interpretation Guide")
        st.markdown("""
        **Confidence Levels:**
        - **90-100%**: Very high confidence
        - **70-89%**: High confidence  
        - **50-69%**: Moderate confidence
        - **Below 50%**: Low confidence - seek more info
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
        "Our revolutionary green technology reduces carbon emissions without any compromise on performance.",
        "Made with sustainable materials that protect the planet for future generations."
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

    # About Us section
    st.markdown('''
    <div class="section-box fade-in-up">
        <div class="section-title">About Us:</div>
        <div class="section-text">
            <div class="section-text">
            <strong>Our Mission:</strong> To democratize access to sustainability information and empower consumers to make informed, environmentally conscious purchasing decisions while holding brands accountable for their environmental claims.
            <br><br>
            <strong>The Problem:</strong> With increasing consumer demand for sustainable products, companies are making more environmental claims than ever. However, many of these claims are misleading, vague, or completely false - a practice known as greenwashing.
            <br><br>
            <strong>Our Solution:</strong> We've developed an AI-powered tool that analyzes sustainability claims using advanced Natural Language Processing, helping consumers identify potentially misleading environmental marketing.
            <br><br>
            <strong>Built by Team BharatWin</strong>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
