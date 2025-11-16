Healthcare Chatbot - Minimal functional prototype
Tech stack: Frontend - HTML/CSS/JS/Bootstrap; Backend - Django; DB - SQLite

Features:
- Simple multilingual (English/Hindi) rule-based responses for safety.
- Emergency keyword detection and escalation message.
- Conversation logging into SQLite (Conversation model).
- Frontend chat UI with Bootstrap; simple session handling.
- Safe template-based medical replies for a few common symptoms (fever, cough).

How to run locally (Windows PowerShell / Mac / Linux):
1. Install Python 3.8+ and pip.
2. (Recommended) Create virtualenv and activate it:
   python -m venv venv
   venv\\Scripts\\activate   (Windows)
   source venv/bin/activate  (Mac/Linux)
3. Install Django:
   pip install django
4. From project root (where manage.py is):
   python manage.py migrate
   python manage.py createsuperuser   # optional to view Conversation in admin
   python manage.py runserver
5. Open http://127.0.0.1:8000/ to use the chatbot.

Notes:
- This is a safety-first minimal prototype (rule-based). It is intentionally constrained
  to avoid giving unverified medical advice. Extend KB in chat/views.py or connect to
  external verified knowledge sources (WHO, CDC) for production use.
- You can export/import the KB or add more languages by editing KB dict in views.py.
