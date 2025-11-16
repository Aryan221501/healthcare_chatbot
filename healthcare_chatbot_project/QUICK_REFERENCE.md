# 🏥 Healthcare Chatbot - Quick Reference

## Start Server
```bash
cd healthcare_chatbot_project
python manage.py runserver
```
Then open: **http://localhost:8000**

## Test AI
```bash
python test_gemini.py
```

## What to Ask

### General Questions
- "Hello" - Get started
- "Help" - See what bot can do
- "Tell me about [condition]" - Learn about diseases
- "What are symptoms of [disease]?" - Symptom information

### Get Diagnosis
- "I have [symptoms], diagnose me" - AI diagnosis
- "Start diagnosis" - Traditional step-by-step
- "What do I have?" - AI will ask questions
- "Can you run a diagnosis?" - Trigger diagnosis mode

### Examples
- "I have a fever and cough, what do I have?"
- "My stomach hurts, diagnose me"
- "I think I have a migraine"
- "Start diagnosis - I have chest pain"

## System Status Indicators

### Console Logs (Good Signs)
```
✅ Gemini API initialized successfully
🤖 Sending request to Gemini AI...
✅ Gemini AI responded successfully
```

### Response Types
- `gemini_ai` - AI chat working
- `gemini_diagnosis` - AI diagnosis working
- `diagnosis_engine` - Traditional diagnosis working
- `rules` - Fallback system (AI not available)

## Quick Fixes

### Not Responding?
1. Check server is running
2. Hard refresh browser (Ctrl+Shift+R)
3. Check console for errors

### AI Not Working?
1. Verify `.env` has `GEMINI_API_KEY`
2. Check internet connection
3. Run `python test_gemini.py`

### Diagnosis Not Working?
1. Use keywords: "diagnose", "what do I have"
2. Try "start diagnosis"
3. Check console logs

## Files Changed

✅ `chat/views.py` - Added diagnosis imports and logic
✅ `chat/gemini_integration.py` - Fixed model name to `gemini-2.5-flash`
✅ `chat/diagnosis_engine.py` - Decision trees for diagnosis

## Key Features

✅ AI-powered responses (Gemini 2.5 Flash)
✅ Medical diagnosis (AI + Traditional)
✅ Emergency detection
✅ Conversation memory
✅ Premium dark mode UI
✅ Bilingual support (EN/HI)

## Emergency Keywords
Bot automatically detects: chest pain, can't breathe, severe bleeding, unconscious, allergic reaction

**Always call 911 for real emergencies!**

---

**Everything is working! Start the server and test it out! 🚀**
