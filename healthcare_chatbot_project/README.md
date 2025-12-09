# 🏥 HealthBot AI - Healthcare Chatbot

An intelligent healthcare chatbot powered by Google Gemini AI with comprehensive medical diagnosis capabilities.

## ✨ Features

- 🤖 **AI-Powered Responses** - Google Gemini 2.5 Flash integration
- 🔍 **Medical Diagnosis** - Interactive diagnosis for 7+ categories
- 💬 **Natural Language** - Understands complex medical questions
- 🌐 **Bilingual Support** - English and Hindi
- 🎨 **Modern UI** - Premium dark theme with emerald accents
- 📱 **Responsive Design** - Works on all devices
- 🔒 **Privacy Focused** - No data collection

## 🚀 Quick Start

### 
1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Setup Gemini API Key

1. Get your FREE API key from: https://makersuite.google.com/app/apikey
2. Copy the `.env.example` file and rename it to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Replace `your_api_key_here` with your actual API key in the `.env` file:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

⚠️ **Important**: Keep your API key secure and never commit the `.env` file to version control.

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Start Server

```bash
python manage.py runserver
```

### 5. Open Browser

Navigate to: http://localhost:8000

## 📁 Project Structure

```
healthcare_chatbot_project/
├── chat/                      # Main app
│   ├── views.py              # API endpoints
│   ├── gemini_integration.py # AI integration
│   ├── diagnosis_engine.py   # Diagnosis logic
│   ├── medical_kb.py         # Medical knowledge base
│   └── comprehensive_diagnosis.py  # Extended diagnosis
├── static/                    # Static files
│   ├── styles.css            # Styling
│   └── chat.js               # Frontend logic
├── templates/                 # HTML templates
│   └── chat/
│       └── index.html        # Main interface
├── healthcare/                # Django settings
├── .env                      # Environment variables
├── manage.py                 # Django management
└── requirements.txt          # Dependencies
```

## 🎯 Usage

### General Questions
- "Hello" - Get started
- "Help" - See available topics
- "What is diabetes?" - Learn about conditions

### Medical Diagnosis
- "I have a fever and cough, diagnose me" - AI diagnosis
- "Start diagnosis" - Interactive yes/no questions

### Available Diagnosis Categories
- 🫁 Respiratory (flu, cold, asthma, bronchitis)
- 🤢 Digestive (stomach issues, GERD, IBS)
- ❤️ Cardiovascular (heart conditions)
- 🧠 Neurological (headaches, migraines)
- 🌿 Dermatological (skin conditions)
- 💙 Mental Health (anxiety, depression)
- 🦴 Musculoskeletal (joint/muscle pain)

## 🛠️ Configuration

### Environment Variables (.env)
```
GEMINI_API_KEY=your_api_key_here
```

### Django Settings
- Database: SQLite (default)
- Debug: True (development)
- Allowed Hosts: localhost

## 🧪 Testing

### Test Gemini Integration
```bash
python quick_test.py
```

### Test Diagnosis System
```bash
python setup_gemini.py
```

## 📚 API Endpoints

### POST /api/message/
Send a message to the chatbot

**Request:**
```json
{
  "text": "I have a fever",
  "session": "optional_session_id"
}
```

**Response:**
```json
{
  "session": "session_id",
  "response": "AI response here",
  "language": "en",
  "powered_by": "gemini_ai"
}
```

## 🎨 Customization

### Change Theme Colors
Edit `static/styles.css`:
```css
:root {
  --dark-accent-primary: #10b981;  /* Emerald green */
  --dark-bg-primary: #0a0e1a;      /* Dark navy */
}
```

### Modify AI Behavior
Edit `chat/gemini_integration.py`:
- Adjust system prompts
- Change temperature/parameters
- Customize response format

## 🔒 Security

- ✅ CSRF protection enabled
- ✅ Environment variables for secrets
- ✅ No sensitive data logging
- ✅ API key not exposed to frontend

## 📝 Important Notes

### Medical Disclaimer
This chatbot provides **general health information only**. It is NOT a substitute for professional medical advice, diagnosis, or treatment.

**Always:**
- Consult healthcare professionals for medical concerns
- Call 911 for emergencies
- Follow your doctor's advice

### API Usage
- Gemini API is **100% FREE**
- 60 requests per minute limit
- No credit card required

## 🐛 Troubleshooting

### Chatbot Not Responding
1. Check `.env` has valid API key
2. Verify server is running
3. Hard refresh browser (Ctrl+Shift+R)
4. Check console for errors

### API Key Issues
1. Get new k
ey from Google AI Studio
2. Verify key starts with "AIza"
3. Check for extra spaces
4. Restart server after adding key

### Database Errors
```bash
python manage.py migrate
python manage.py makemigrations
```

## 📦 Dependencies

- Django 4.2+
- google-generativeai
- python-dotenv
- Bootstrap 5.3
- Bootstrap Icons

## 🤝 Contributing

This is a healthcare education project. Feel free to:
- Report bugs
- Suggest features
- Improve documentation
- Add medical knowledge

## 📄 License

Educational project - Use responsibly

## 🔗 Links

- Google AI Studio: https://makersuite.google.com/app/apikey
- Django Docs: https://docs.djangoproject.com/
- Gemini API: https://ai.google.dev/

## 👨‍💻 Development

### Run in Development
```bash
python manage.py runserver
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Access Admin
http://localhost:8000/admin

## 🎓 Learning Resources

- Medical knowledge base in `chat/medical_kb.py`
- Diagnosis trees in `chat/diagnosis_engine.py`
- AI prompts in `chat/gemini_integration.py`

---

**Built with ❤️ for healthcare education**

**Version:** 1.0.0  
**Last Updated:** 2025  
**Status:** ✅ Production Ready
