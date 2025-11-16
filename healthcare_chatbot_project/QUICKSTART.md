# 🚀 Quick Start Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Installation & Setup

### 1. Install Dependencies
```bash
cd healthcare_chatbot_project
pip install -r requirements.txt
```

### 2. Run Database Migrations (if needed)
```bash
python manage.py migrate
```

### 3. Start the Development Server
```bash
python manage.py runserver
```

### 4. Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

## 🎨 What's New

### Premium Dark Mode
- Beautiful gradient background with animated particles
- Glassmorphism effects on all cards
- Smooth animations throughout the interface

### Enhanced AJAX
- Real-time messaging without page reloads
- Connection status monitoring
- Realistic typing indicators
- Error handling with user feedback

### Animations
- Page load animation with loading screen
- Message slide-in effects
- Button hover and ripple effects
- Smooth transitions everywhere

### User Experience
- Click to copy messages
- Keyboard shortcuts (Ctrl+K, Ctrl+L)
- Quick action buttons with icons
- Auto-resizing textarea
- Timestamps on messages

## 🎯 Features to Try

1. **Send a message** - Type and press Enter or click Send
2. **Use quick actions** - Click the Fever, Cough, Emergency, or Help buttons
3. **Copy messages** - Click any message bubble to copy its text
4. **Clear chat** - Click the Clear button or press Ctrl+L
5. **Switch language** - Use the Language dropdown in the navbar
6. **Keyboard shortcuts** - Press Ctrl+K to focus the input

## 📱 Responsive Design

The interface automatically adapts to:
- 📱 Mobile devices (< 576px)
- 📱 Tablets (577px - 991px)
- 💻 Desktops (> 992px)

## 🎨 Customization

### Colors
Edit `static/styles.css` and modify the CSS variables in `:root`:
```css
:root {
  --dark-accent-primary: #667eea;
  --dark-accent-secondary: #764ba2;
  /* ... more variables */
}
```

### Animations
Adjust animation speeds in the CSS variables:
```css
--transition-fast: 0.2s;
--transition-normal: 0.3s;
--transition-slow: 0.5s;
```

## 🐛 Troubleshooting

### Static files not loading?
```bash
python manage.py collectstatic
```

### Port already in use?
```bash
python manage.py runserver 8080
```

### Database issues?
```bash
python manage.py migrate --run-syncdb
```

## 📚 Documentation

- See `FEATURES.md` for detailed feature list
- Check `README.md` for project overview
- Review `chat/views.py` for backend logic

## 🎉 Enjoy!

Your premium dark mode healthcare chatbot is ready to use!
