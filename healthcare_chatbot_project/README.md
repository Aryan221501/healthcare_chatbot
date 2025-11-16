# Healthcare Chatbot

A comprehensive healthcare chatbot application built with Django, featuring both rule-based responses and AI-powered medical assistance through Google's Gemini API.

## 🚀 Features

- **Multilingual Support**: English and Hindi with capability to add more languages
- **AI-Powered Responses**: Integration with Google Gemini API for intelligent responses
- **Emergency Detection**: Automatic detection of emergency keywords with appropriate escalation
- **Conversation Logging**: All interactions are stored in SQLite database
- **Responsive UI**: Bootstrap-based frontend with modern design
- **Medical Diagnosis**: AI-powered symptom-based diagnosis assistance
- **Typing Animation**: Enhanced user experience with typing indicators
- **Dark Mode**: Comfortable viewing in low-light environments

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (with capability to scale to PostgreSQL/MySQL)
- **AI Integration**: Google Gemini API
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Aryan221501/healthcare_chatbot.git
cd healthcare_chatbot
```

### 2. Set up virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API keys
- Get your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)
- Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```
- Add your API key to the `.env` file:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

> ⚠️ **Security Warning**: Never commit your actual API keys to version control. The `.env` file is included in `.gitignore` for security.

### 5. Set up the database
```bash
python manage.py migrate
python manage.py createsuperuser  # Optional: to access admin panel
```

### 6. Run the application
```bash
python manage.py runserver
```

### 7. Access the application
Open your browser and go to `http://127.0.0.1:8000/`

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root with the following:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### Settings
The application configuration is in `healthcare/settings.py`. You can modify:
- Database settings
- Security settings
- Static files configuration
- API timeouts and limits

## 🧪 Testing

Run the test suite to ensure everything is working properly:
```bash
python manage.py test
```

## 📁 Project Structure

```
healthcare_chatbot/
├── chat/                 # Chat functionality and AI integration
│   ├── views.py          # Main application logic
│   ├── models.py         # Data models
│   ├── gemini_integration.py  # Google Gemini API integration
│   └── chatgpt_integration.py # OpenAI ChatGPT integration (fallback)
├── healthcare/           # Django project settings
│   └── settings.py       # Configuration settings
├── templates/            # HTML templates
├── static/               # CSS, JavaScript, images
├── .env                 # Environment variables (not committed)
├── .env.example         # Template for environment variables
├── manage.py            # Django management commands
└── requirements.txt     # Python dependencies
```

## ⚠️ Important Notes

- This is a healthcare assistant, not a diagnostic tool. Always recommend professional medical consultation.
- The application includes safety measures to avoid providing unverified medical advice.
- For production use, connect to verified medical knowledge sources (WHO, CDC, etc.).
- Ensure compliance with healthcare data privacy regulations (HIPAA, etc.) before production deployment.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## 🐛 Troubleshooting

See `TROUBLESHOOTING.md` for common issues and solutions.

For API integration issues, check `GEMINI_INTEGRATED.md` and `CHATGPT_INTEGRATION.md`.

## 📞 Support

For support, please open an issue in the GitHub repository.