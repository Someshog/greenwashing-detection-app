"""
Simple example demonstrating the greenwashing detection functionality
"""
from transformers import pipeline
import time

def demo_greenwashing_detection():
    """Demonstrate the greenwashing detection with example claims"""
    
    print("🌱 Greenwashing Detection Demo")
    print("=" * 40)
    
    # Load the model
    print("Loading AI model... (This may take a moment)")
    try:
        classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        print("✅ Model loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return
    
    # Example claims to test
    test_claims = [
        {
            "claim": "Our product is eco-friendly and good for the environment.",
            "expected": "Likely Greenwashing (vague claims)"
        },
        {
            "claim": "We use 100% certified organic cotton sourced from fair-trade farms with verified supply chain transparency.",
            "expected": "Likely Genuine (specific, verifiable claims)"
        },
        {
            "claim": "This item is natural and green.",
            "expected": "Likely Greenwashing (vague terms)"
        },
        {
            "claim": "Our manufacturing process is powered by 100% renewable energy with third-party verified carbon offsets.",
            "expected": "Likely Genuine (specific, verifiable claims)"
        }
    ]
    
    # Classification labels
    candidate_labels = ["Greenwashing", "Genuine Sustainability"]
    
    print("\n🔍 Analyzing Claims:")
    print("=" * 40)
    
    for i, test_case in enumerate(test_claims, 1):
        print(f"\n{i}. Claim: \"{test_case['claim']}\"")
        print(f"   Expected: {test_case['expected']}")
        
        try:
            # Perform classification
            result = classifier(test_case['claim'], candidate_labels)
            
            # Display results
            prediction = result['labels'][0]
            confidence = result['scores'][0]
            
            print(f"   🤖 AI Prediction: {prediction}")
            print(f"   📊 Confidence: {confidence:.2%}")
            
            # Show confidence for both labels
            print("   📈 All Scores:")
            for label, score in zip(result['labels'], result['scores']):
                print(f"      - {label}: {score:.2%}")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 40)
    print("Demo completed! Run the Streamlit app for the full interactive experience.")
    print("Command: streamlit run app.py")

if __name__ == "__main__":
    demo_greenwashing_detection()
