# 🔧 Chatbot Not Responding - Troubleshooting Guide

## Quick Diagnosis

### Step 1: Check if Server is Running
Make sure Django server is running:
```bash
cd healthcare_chatbot_project
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 2: Open Test Page
Open `test_api.html` in your browser to diagnose the issue:
1. Right-click on `test_api.html`
2. Select "Open with" → Your browser
3. Click all test buttons to see what's failing

### Step 3: Check Browser Console
1. Open the chatbot: `http://127.0.0.1:8000/`
2. Press `F12` to open Developer Tools
3. Go to "Console" tab
4. Try sending a message
5. Look for error messages (red text)

---

## Common Issues & Solutions

### Issue 1: CSRF Token Error

**Symptoms:**
- Console shows: "403 Forbidden"
- Console shows: "CSRF verification failed"

**Solution:**
I've already added CSRF token to the form. Just restart the server:
```bash
# Stop server: Ctrl + C
# Start again:
python manage.py runserver
```

Then hard refresh browser: `Ctrl + Shift + R`

---

### Issue 2: Server Not Running

**Symptoms:**
- Console shows: "Failed to fetch"
- Console shows: "net::ERR_CONNECTION_REFUSED"
- Page doesn't load at all

**Solution:**
Start the Django server:
```bash
cd healthcare_chatbot_project
python manage.py runserver
```

---

### Issue 3: Wrong URL

**Symptoms:**
- Console shows: "404 Not Found"
- API endpoint not found

**Solution:**
Make sure you're visiting the correct URL:
- ✅ Correct: `http://127.0.0.1:8000/`
- ❌ Wrong: `http://localhost:8000/`
- ❌ Wrong: Opening HTML file directly

---

### Issue 4: Database Not Migrated

**Symptoms:**
- Console shows: "no such table: chat_conversation"
- Server shows database errors

**Solution:**
Run migrations:
```bash
cd healthcare_chatbot_project
python manage.py makemigrations
python manage.py migrate
```

---

### Issue 5: JavaScript Not Loading

**Symptoms:**
- Nothing happens when clicking Send
- No console errors
- Typing indicator doesn't show

**Solution:**
Hard refresh to reload JavaScript:
- Windows/Linux: `Ctrl + Shift + R`
- Mac: `Cmd + Shift + R`

Or clear cache and reload.

---

### Issue 6: Port Already in Use

**Symptoms:**
- Server shows: "Error: That port is already in use"

**Solution:**
Use a different port:
```bash
python manage.py runserver 8080
```

Then visit: `http://127.0.0.1:8080/`

---

## Detailed Debugging Steps

### 1. Check Server Logs
Look at the terminal where Django is running. You should see:
```
[17/Nov/2025 10:30:00] "GET / HTTP/1.1" 200 5432
[17/Nov/2025 10:30:05] "POST /api/message/ HTTP/1.1" 200 123
```

If you see errors, they'll appear here.

### 2. Test API Directly
Open this URL in your browser:
```
http://127.0.0.1:8000/api/message/
```

You should see:
```json
{"error": "POST required"}
```

This confirms the API endpoint exists.

### 3. Check Browser Network Tab
1. Open Developer Tools (F12)
2. Go to "Network" tab
3. Send a message in the chatbot
4. Look for `/api/message/` request
5. Click on it to see details:
   - Status should be 200
   - Response should have JSON data

### 4. Check Console Logs
I've added detailed logging. You should see:
```
Sending message: I have a fever
Session: abc-123-def
CSRF Token: Found
Response status: 200
Response data: {session: "...", response: "...", language: "en"}
```

If you don't see these logs, JavaScript isn't running.

---

## Manual Test

### Test 1: Send Message via Console
Open browser console (F12) and run:
```javascript
fetch('/api/message/', {
  method: 'POST',
  body: new FormData(document.getElementById('chatForm')),
  credentials: 'same-origin'
}).then(r => r.json()).then(console.log);
```

Then type in the input and run:
```javascript
document.getElementById('textInput').value = 'test';
document.getElementById('chatForm').dispatchEvent(new Event('submit'));
```

### Test 2: Check if Chatbot Instance Exists
In console, run:
```javascript
console.log(chatbotInstance);
```

Should show: `HealthcareChatbot {session: "", ...}`

If it shows `undefined`, JavaScript didn't initialize.

---

## Files to Check

### 1. views.py
Should have:
```python
@ensure_csrf_cookie
def index(request):
    return render(request, 'chat/index.html', {})

def message_api(request):
    if request.method=='POST':
        text = request.POST.get('text','').strip()
        # ... rest of code
```

### 2. index.html
Should have:
```html
<form id="chatForm">
  {% csrf_token %}
  <div class="input-group">
    <textarea id="textInput" ...></textarea>
    <button id="sendButton" ...>Send</button>
  </div>
</form>
```

### 3. chat.js
Should have:
```javascript
async postMessage(text, session = '') {
  const formData = new FormData();
  formData.append('text', text);
  // ... rest of code
}
```

---

## Still Not Working?

### Nuclear Option
1. Stop the server (Ctrl + C)
2. Close all browser windows
3. Restart your computer
4. Start server:
   ```bash
   cd healthcare_chatbot_project
   python manage.py runserver
   ```
5. Open browser in Incognito mode
6. Go to: `http://127.0.0.1:8000/`
7. Open console (F12) and watch for errors
8. Try sending a message

### Get Help
If still not working, check:
1. Server terminal for errors
2. Browser console for errors
3. Network tab for failed requests
4. Run `test_api.html` to diagnose

Take a screenshot of any errors and check:
- What's the error message?
- What's the status code?
- What's in the server logs?

---

## Expected Behavior

When working correctly:

1. **Type message** → Send button enables
2. **Click Send** → Message appears in chat
3. **Typing indicator** → Shows "Preparing response"
4. **After 2-3 seconds** → Bot response appears
5. **Console logs** → Show successful request/response

---

## Quick Checklist

- [ ] Django server is running
- [ ] Visiting correct URL (127.0.0.1:8000)
- [ ] Browser console shows no errors
- [ ] Hard refreshed browser (Ctrl+Shift+R)
- [ ] CSRF token is present in form
- [ ] JavaScript file is loading
- [ ] API endpoint exists (/api/message/)
- [ ] Database is migrated
- [ ] test_api.html shows all tests passing

If all checked and still not working, there might be a deeper issue. Check the server logs carefully.

---

## Success Indicators

✅ Server running without errors
✅ Page loads correctly
✅ Can type in input field
✅ Send button enables when typing
✅ Clicking Send shows typing indicator
✅ Bot responds after a few seconds
✅ Console shows successful API calls
✅ No red errors in console

**Your chatbot should now be responding! 🎉**
