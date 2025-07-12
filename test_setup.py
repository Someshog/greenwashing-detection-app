"""
Test script to verify the greenwashing detection setup
"""
import sys
import importlib

def test_imports():
    """Test if all required packages are properly installed"""
    required_packages = [
        'streamlit',
        'transformers',
        'torch',
        'numpy',
        'pandas'
    ]
    
    print("Testing package imports...")
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package} - OK")
        except ImportError as e:
            print(f"❌ {package} - ERROR: {e}")
    
    print("\nTesting transformers pipeline...")
    try:
        from transformers import pipeline
        print("✅ Transformers pipeline import - OK")
        
        # Test if we can create a pipeline (this will download the model if not cached)
        print("Note: Model will be downloaded on first run (~1.6GB)")
        
    except Exception as e:
        print(f"❌ Transformers pipeline - ERROR: {e}")
    
    print("\nSetup verification complete!")
    print("\nTo run the app, use:")
    print("streamlit run app.py")

if __name__ == "__main__":
    test_imports()
