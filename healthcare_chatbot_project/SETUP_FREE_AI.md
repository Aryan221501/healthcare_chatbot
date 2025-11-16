# 🆓 FREE AI Setup Guide - Google Gemini

## Why Google Gemini?
- ✅ **100% FREE** (60 requests per minute)
- ✅ No credit card required
- ✅ High quality responses
- ✅ Easy to set up (5 minutes)
- ✅ Comparable to ChatGPT

---

## 🚀 Quick Setup (5 Minutes)

### Step 1: Get FREE API Key

1. Go to: **https://makersuite.google.com/app/apikey**
2. Sign in with Google account
3. Click **"Create API Key"**
4. Copy the key (starts with `AIza...`)

**That's it! No credit card needed!** 🎉

### Step 2: Install Package

```bash
cd healthcare_chatbot_project
pip install google-generativeai
```

### Step 3: Create .env File

Create `.env` file in `healthcare_chatbot_project` folder:

```bash
# .env
GEMINI_API_KEY=AIza-your-key-here
```

Replace with your actual key!

### Step 4: Update requirements.txt

Add to `requirements.txt`:

```
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

### Step 5: Update settings.py

Add to `healthcare/settings.py`:

```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add Gemini API key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
```

### Step 6: Update views.py

Replace `message_api` function in `chat/views.py`:

```python
from .gemini_integration import get_gemini_response, is_gemini_available

# Store conversation history
conversation_histories = {}

def message_api(request):
    if request.method=='POST':
        try:
            text = request.POST.get('text','').strip()
            if not text:
                return JsonResponse({'error': 'No text provided'}, status=400)
            
            session = request.POST.get('session','')
            if not session:
                session = str(uuid.uuid4())
            
            lang = detect_language(text)
            
            # Try Gemini first if available (FREE!)
            if is_gemini_available():
                # Get conversation history
                history = conversation_histories.get(session, [])
                
                # Get Gemini response
                response = get_gemini_response(text, history)
                
                if response:
                    # Update conversation history
                    history.append({"role": "user", "content": text})
                    history.append({"role": "assistant", "content": response})
                    conversation_histories[session] = history[-10:]
                else:
                    # Fallback to rule-based
                    response = match_kb(lang, text)
            else:
                # Use rule-based system
                response = match_kb(lang, text)
            
            # Save to database
            try:
                Conversation.objects.create(
                    session_id=session,
                    user_text=text,
                    bot_text=response,
                    language=lang
                )
            except Exception as db_error:
                print(f"Database error: {db_error}")
            
            return JsonResponse({
                'session': session,
                'response': response,
                'language': lang
            })
            
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'POST required'}, status=400)
```

### Step 7: Test It!

```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000/` and try:
- "What are the symptoms of diabetes?"
- "I have a headache, what should I do?"
- "How can I manage stress?"

---

## ✅ Verification

Test in Python shell:

```bash
python manage.py shell
```

```python
from chat.gemini_integration import get_gemini_response

response = get_gemini_response("Hello, I have a fever")
print(response)
```

If you see a detailed response, it's working! 🎉

---

## 🔧 Troubleshooting

### Error: "Module 'google.generativeai' not found"
```bash
pip install google-generativeai
```

### Error: "Invalid API key"
- Check your API key in `.env` file
- Make sure it starts with `AIza`
- No extra spaces

### Error: "Module 'dotenv' not found"
```bash
pip install python-dotenv
```

### Gemini not responding
- Check if `.env` file exists
- Verify `GEMINI_API_KEY` in settings.py
- Check server logs for errors

---

## 💰 FREE Limits

### Google Gemini FREE Tier:
- **60 requests per minute** (very generous!)
- **1,500 requests per day**
- **1 million tokens per month**

**This is MORE than enough for most chatbots!**

For a typical chatbot:
- 1 conversation = ~1 request
- You can handle **1,500 conversations per day**
- **45,000 conversations per month**

**Completely FREE!** 🎉

---

## 📊 Comparison

### Before (Rule-Based):
```
User: What should I do for a fever?
Bot: If you have a fever, rest, stay hydrated and monitor temperature.
```

### After (FREE Gemini AI):
```
User: What should I do for a fever?
Bot: 🌡️ Here's what you should do for a fever:

**Immediate Actions:**
• Rest and avoid strenuous activities
• Drink plenty of fluids (water, herbal tea, clear broths)
• Take acetaminophen (Tylenol) or ibuprofen (Advil) as directed
• Wear light, comfortable clothing
• Use a lukewarm compress on your forehead

**Monitor Your Temperature:**
• Check every 4-6 hours
• Normal: 97-99°F (36.1-37.2°C)
• Fever: >100.4°F (38°C)

**When to See a Doctor:**
• Fever >103°F (39.4°C)
• Lasts more than 3 days
• Accompanied by severe headache, stiff neck, or rash
• Difficulty breathing

**For Children:**
• Fever >100.4°F in infants <3 months - seek immediate care

Would you like more specific advice?

*Disclaimer: This is general information. Please consult a healthcare provider for personalized medical advice.*
```

**Much better, and completely FREE!** 🎉

---

## 🎯 What You Get (FREE!)

✅ Natural language understanding
✅ Conversational responses
✅ Context awareness
✅ Intelligent medical guidance
✅ Handles complex queries
✅ More human-like interactions
✅ **No cost at all!**

---

## 🔒 Security

1. Add to `.gitignore`:
```
.env
*.env
```

2. Never commit API keys to Git

3. Keep your API key private

---

## 🎉 You're Done!

Your chatbot now has:
- ✅ FREE AI integration
- ✅ Intelligent responses
- ✅ Natural conversations
- ✅ No cost!

**Enjoy your FREE AI-powered chatbot!** 🚀

---

## 📝 Quick Checklist

- [ ] Get Gemini API key from https://makersuite.google.com/app/apikey
- [ ] Install: `pip install google-generativeai python-dotenv`
- [ ] Create `.env` file with `GEMINI_API_KEY=your-key`
- [ ] Update `settings.py` to load API key
- [ ] Update `views.py` to use Gemini
- [ ] Add `.env` to `.gitignore`
- [ ] Test with `python manage.py runserver`

**That's it! Your chatbot is now AI-powered for FREE!** 🎉
