# 🚀 ChatGPT Setup Guide

## Quick Setup (5 Minutes)

### Step 1: Get OpenAI API Key

1. Go to https://platform.openai.com/
2. Sign up or log in
3. Click on your profile (top right)
4. Select "View API keys"
5. Click "Create new secret key"
6. **Copy the key immediately** (you won't see it again!)

### Step 2: Install Required Packages

```bash
cd healthcare_chatbot_project
pip install openai python-dotenv
```

### Step 3: Create .env File

Create a file named `.env` in the `healthcare_chatbot_project` folder:

```bash
# .env
OPENAI_API_KEY=sk-your-api-key-here
```

**Replace `sk-your-api-key-here` with your actual API key!**

### Step 4: Update requirements.txt

Add these lines to `requirements.txt`:

```
openai>=1.0.0
python-dotenv>=1.0.0
```

### Step 5: Update settings.py

Add to `healthcare/settings.py` (at the top):

```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add after other settings
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
```

### Step 6: Update .gitignore

Add to `.gitignore` (create if doesn't exist):

```
.env
*.env
__pycache__/
*.pyc
db.sqlite3
```

### Step 7: Update views.py

Replace the `message_api` function in `chat/views.py`:

```python
from .chatgpt_integration import get_chatgpt_response, is_chatgpt_available

# Store conversation history (use database in production)
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
            
            # Try ChatGPT first if available
            if is_chatgpt_available():
                # Get conversation history
                history = conversation_histories.get(session, [])
                
                # Get ChatGPT response
                response = get_chatgpt_response(text, history)
                
                if response:
                    # Update conversation history
                    history.append({"role": "user", "content": text})
                    history.append({"role": "assistant", "content": response})
                    conversation_histories[session] = history[-10:]  # Keep last 10 messages
                else:
                    # Fallback to rule-based if ChatGPT fails
                    response = match_kb(lang, text)
            else:
                # Use rule-based system if ChatGPT not available
                response = match_kb(lang, text)
            
            # Try to save to database
            try:
                Conversation.objects.create(session_id=session, user_text=text, bot_text=response, language=lang)
            except Exception as db_error:
                print(f"Database error (non-critical): {db_error}")
            
            return JsonResponse({'session': session, 'response': response, 'language': lang})
        except Exception as e:
            print(f"Error in message_api: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error':'POST required'}, status=400)
```

### Step 8: Test It!

```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000/` and try:
- "What are the symptoms of diabetes?"
- "I have a headache, what should I do?"
- "Explain how vaccines work"

---

## ✅ Verification

### Test if ChatGPT is working:

```python
# In Python shell
python manage.py shell

>>> from chat.chatgpt_integration import get_chatgpt_response
>>> response = get_chatgpt_response("Hello, I have a fever")
>>> print(response)
```

If you see a detailed response, it's working! 🎉

---

## 🔧 Troubleshooting

### Error: "Invalid API key"
- Check your API key in `.env` file
- Make sure there are no extra spaces
- Verify key starts with `sk-`

### Error: "Module 'openai' not found"
```bash
pip install openai
```

### Error: "Module 'dotenv' not found"
```bash
pip install python-dotenv
```

### ChatGPT not responding
- Check if `.env` file exists
- Verify `OPENAI_API_KEY` is set in settings.py
- Check server logs for errors
- Verify you have API credits (check OpenAI dashboard)

### Responses are slow
- Normal! ChatGPT takes 2-5 seconds
- Consider using GPT-3.5-turbo (faster than GPT-4)
- Add loading indicator in UI

---

## 💰 Cost Management

### Check Usage:
1. Go to https://platform.openai.com/usage
2. View your API usage and costs
3. Set up billing alerts

### Set Spending Limits:
1. Go to https://platform.openai.com/account/billing/limits
2. Set monthly budget limit
3. Get email alerts

### Typical Costs:
- **100 conversations:** ~$0.10 (10 cents)
- **1,000 conversations:** ~$1.00
- **10,000 conversations:** ~$10.00

Very affordable for most use cases!

---

## 🎯 What's Next?

### Your chatbot now has:
✅ Natural language understanding
✅ Conversational responses
✅ Context awareness
✅ Intelligent medical guidance
✅ Fallback to rule-based system

### Try these queries:
- "Explain the difference between cold and flu"
- "What should I eat if I have diabetes?"
- "How can I manage stress and anxiety?"
- "Tell me about high blood pressure"

---

## 🔒 Security Reminders

1. ✅ Never commit `.env` file to Git
2. ✅ Add `.env` to `.gitignore`
3. ✅ Don't share your API key
4. ✅ Rotate keys if exposed
5. ✅ Monitor usage regularly

---

## 📊 Comparison

### Before (Rule-Based):
```
User: What should I do if I have a fever?
Bot: If you have a fever, rest, stay hydrated and monitor temperature.
```

### After (ChatGPT):
```
User: What should I do if I have a fever?
Bot: 🌡️ Here's what you should do for a fever:

**Immediate Actions:**
• Rest and avoid physical activity
• Drink plenty of fluids (water, herbal tea, clear broths)
• Take acetaminophen (Tylenol) or ibuprofen (Advil) as directed
• Wear light, breathable clothing
• Use a lukewarm compress on your forehead

**Monitor Your Temperature:**
• Check every 4-6 hours
• Normal: 97-99°F (36.1-37.2°C)
• Fever: >100.4°F (38°C)

**When to See a Doctor:**
• Fever >103°F (39.4°C)
• Lasts more than 3 days
• Accompanied by severe headache, rash, or difficulty breathing

**For Children:**
• Fever >100.4°F in infants <3 months - seek immediate care
• Persistent crying or unusual behavior

Would you like more specific advice based on your symptoms?

*Disclaimer: This is general information. Please consult a healthcare provider for personalized medical advice.*
```

Much better, right? 🎉

---

**You're all set! Your chatbot is now powered by ChatGPT!** 🚀
