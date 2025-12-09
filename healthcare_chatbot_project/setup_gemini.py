"""
Interactive script to setup Gemini API key
"""

import os
import sys

print("=" * 70)
print("🔑 GEMINI API KEY SETUP")
print("=" * 70)
print()
print("To use Gemini AI (100% FREE), you need an API key.")
print()
print("📋 Steps to get your FREE API key:")
print()
print("1. Visit: https://makersuite.google.com/app/apikey")
print("   OR: https://aistudio.google.com/app/apikey")
print()
print("2. Sign in with your Google account")
print()
print("3. Click 'Create API Key' button")
print()
print("4. Copy the generated key (starts with 'AIza...')")
print()
print("=" * 70)
print()

# Get API key from user
api_key = input("Paste your Gemini API key here: ").strip()

if not api_key:
    print("\n❌ No API key provided. Exiting...")
    sys.exit(1)

if not api_key.startswith('AIza'):
    print("\n⚠️  Warning: API key should start with 'AIza'")
    confirm = input("Continue anyway? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Exiting...")
        sys.exit(1)

# Write to .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')

try:
    with open(env_path, 'w') as f:
        f.write("# Google Gemini API Key (FREE!)\n")
        f.write(f"GEMINI_API_KEY={api_key}\n")
    
    print("\n✅ API key saved to .env file!")
    print()
    print("=" * 70)
    print("🧪 TESTING API KEY...")
    print("=" * 70)
    print()
    
    # Test the API key
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')
    django.setup()
    
    from chat.gemini_integration import get_gemini_response, is_gemini_available
    
    if is_gemini_available():
        print("✅ Gemini API is available!")
        print()
        print("Testing with a simple message...")
        print()
        
        response = get_gemini_response("Hello, this is a test message. Please respond briefly.")
        
        if response:
            print("✅ SUCCESS! Gemini AI is working!")
            print()
            print(f"Response: {response[:200]}...")
            print()
            print("=" * 70)
            print("🎉 SETUP COMPLETE!")
            print("=" * 70)
            print()
            print("You can now start the server:")
            print("  python manage.py runserver")
            print()
            print("Then open: http://localhost:8000")
            print()
        else:
            print("❌ API key is valid but no response received")
            print("This might be a temporary issue. Try again later.")
    else:
        print("❌ Could not initialize Gemini API")
        print("Please check your API key and try again.")
        
except Exception as e:
    print(f"\n❌ Error: {e}")
    print()
    print("Please try again or check the documentation.")
