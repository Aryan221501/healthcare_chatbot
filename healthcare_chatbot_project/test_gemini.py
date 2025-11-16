"""
Test script to verify Gemini AI integration
Run this to check if Gemini is working properly
"""

import os
import sys
import django

# Setup Django environment
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')
django.setup()

from chat.gemini_integration import initialize_gemini, get_gemini_response, is_gemini_available

print("=" * 60)
print("🧪 TESTING GEMINI AI INTEGRATION")
print("=" * 60)

# Test 1: Check if Gemini is available
print("\n📋 Test 1: Checking Gemini availability...")
if is_gemini_available():
    print("✅ Gemini is available and configured!")
else:
    print("❌ Gemini is NOT available. Check your API key in .env file")
    sys.exit(1)

# Test 2: Simple greeting
print("\n📋 Test 2: Testing simple greeting...")
response = get_gemini_response("Hello, how are you?")
if response:
    print(f"✅ Response received:")
    print(f"   {response[:200]}...")
else:
    print("❌ No response received")

# Test 3: Medical question
print("\n📋 Test 3: Testing medical question...")
response = get_gemini_response("What are the symptoms of flu?")
if response:
    print(f"✅ Response received:")
    print(f"   {response[:200]}...")
else:
    print("❌ No response received")

# Test 4: Conversation with history
print("\n📋 Test 4: Testing conversation with history...")
history = [
    {"role": "user", "content": "I have a headache"},
    {"role": "assistant", "content": "I understand you have a headache. Can you tell me more about it?"}
]
response = get_gemini_response("It's been hurting for 2 days", history)
if response:
    print(f"✅ Response received:")
    print(f"   {response[:200]}...")
else:
    print("❌ No response received")

print("\n" + "=" * 60)
print("🎉 GEMINI AI INTEGRATION TEST COMPLETE!")
print("=" * 60)
print("\nIf all tests passed, Gemini is working correctly!")
print("If any tests failed, check:")
print("  1. Your .env file has GEMINI_API_KEY set")
print("  2. The API key is valid (get one from https://makersuite.google.com/app/apikey)")
print("  3. You have internet connection")
print("  4. google-generativeai package is installed (pip install google-generativeai)")
