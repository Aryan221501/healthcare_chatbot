"""Quick test to verify Gemini AI is working"""
import os, sys, django

sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')
django.setup()

from chat.gemini_integration import get_gemini_response, is_gemini_available

print("=" * 60)
print("🧪 QUICK GEMINI TEST")
print("=" * 60)

if is_gemini_available():
    print("✅ Gemini is available!")
    response = get_gemini_response("Hello, test message")
    if response:
        print(f"✅ Response received: {response[:100]}...")
        print("\n✅ GEMINI IS WORKING!")
    else:
        print("❌ No response")
else:
    print("❌ Gemini not available")

print("=" * 60)
