# 🚨 QUICK FIX - Chatbot Not Responding

## The Problem
The chatbot shows "Preparing response" but never gets a reply, then shows an error.

## SOLUTION (Do These Steps in Order)

### Step 1: Check if Server is Running ⚠️ MOST IMPORTANT
Open your terminal and make sure you see this:
```
Starting development server at http://127.0.0.1:8000/
```

If you DON'T see this, the server is not running!

**Start the server:**
```bash
cd healthcare_chatbot_project
python manage.py runserver
```

### Step 2: Check Browser Console
1. Press `F12` to open Developer Tools
2. Go to "Console" tab
3. Look for these messages when you send a message:
   - "Sending message: ..." ✅
   - "CSRF Token: Found" ✅
   - "Response status: 200" ✅
   - "Response data: {...}" ✅

**If you see "Failed to fetch":**
- Server is not running! Go back to Step 1

**If you see "403 Forbidden":**
- CSRF token issue. Do Step 3

**If you see "404 Not Found":**
- Wrong URL. Make sure you're at `http://127.0.0.1:8000/`

### Step 3: Fix CSRF Token Issue
```bash
# Stop server: Ctrl + C
# Start again:
python manage.py runserver
```

Then in browser:
- Hard refresh: `Ctrl + Shift + R` (Windows) or `Cmd + Shift + R` (Mac)

### Step 4: Check Database
If server shows database errors:
```bash
cd healthcare_chatbot_project
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Test with Simple Message
1. Go to `http://127.0.0.1:8000/`
2. Type: `hello`
3. Click Send
4. Should respond in 1-2 seconds

---

## Still Not Working?

### Check Server Terminal
Look at the terminal where Django is running. When you send a message, you should see:
```
[17/Nov/2025 01:32:00] "POST /api/message/ HTTP/1.1" 200 123
```

**If you see nothing:**
- Server is not receiving the request
- Check if you're on the right URL

**If you see errors:**
- Read the error message
- It will tell you what's wrong

### Check Browser Network Tab
1. Press `F12`
2. Go to "Network" tab
3. Send a message
4. Look for `/api/message/` in the list
5. Click on it
6. Check:
   - Status: Should be 200
   - Response: Should have JSON data

---

## Common Errors & Fixes

### Error: "Failed to fetch"
**Cause:** Server not running
**Fix:** Start Django server (Step 1)

### Error: "403 Forbidden"
**Cause:** CSRF token missing
**Fix:** Restart server + hard refresh (Step 3)

### Error: "404 Not Found"
**Cause:** Wrong URL or API endpoint not found
**Fix:** 
- Check URL is `http://127.0.0.1:8000/`
- Check `chat/urls.py` has the API route

### Error: "500 Internal Server Error"
**Cause:** Server-side error
**Fix:** Check server terminal for error details

---

## Test if API Works

### Method 1: Direct URL Test
Open this in your browser:
```
http://127.0.0.1:8000/api/message/
```

Should show:
```json
{"error": "POST required"}
```

If you see this, the API endpoint exists! ✅

### Method 2: Console Test
Open browser console (F12) and run:
```javascript
fetch('/api/message/', {
  method: 'POST',
  body: new URLSearchParams({text: 'hello'}),
  credentials: 'same-origin'
}).then(r => r.json()).then(console.log);
```

Should show:
```javascript
{session: "...", response: "Hello! How can I help...", language: "en"}
```

---

## Nuclear Option (If Nothing Works)

1. **Stop everything:**
   - Close all browser windows
   - Stop Django server (Ctrl + C)

2. **Clean start:**
   ```bash
   cd healthcare_chatbot_project
   python manage.py migrate
   python manage.py runserver
   ```

3. **Fresh browser:**
   - Open browser in Incognito mode
   - Go to `http://127.0.0.1:8000/`
   - Press F12 to open console
   - Try sending a message
   - Watch console for errors

4. **Check both:**
   - Browser console (F12)
   - Server terminal
   - One of them will show the error

---

## What Should Happen (Normal Flow)

1. Type "hello" → Send button enables ✅
2. Click Send → Message appears ✅
3. Typing indicator shows ✅
4. After 1-2 seconds → Bot responds ✅
5. Console shows: "Response status: 200" ✅

---

## Get More Help

If still not working, check:

1. **Server terminal** - Any errors?
2. **Browser console** - Any red errors?
3. **Network tab** - Is request being sent?
4. **URL** - Are you on 127.0.0.1:8000?

Take a screenshot of:
- The error message
- Browser console
- Server terminal

This will help diagnose the issue!

---

## Quick Checklist

- [ ] Django server is running (see "Starting development server...")
- [ ] Visiting http://127.0.0.1:8000/ (not localhost, not file://)
- [ ] Browser console shows no red errors
- [ ] Hard refreshed browser (Ctrl+Shift+R)
- [ ] Can see "Sending message" in console when clicking Send
- [ ] Server terminal shows POST request when sending message

**If all checked, it should work!** 🎉
