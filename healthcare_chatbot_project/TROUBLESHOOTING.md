# 🔧 Troubleshooting Guide

## Issue: Old UI Still Showing After Updates

If you're still seeing the old purple-blue gradient UI instead of the new dark mode, try these solutions:

---

## Solution 1: Hard Refresh Browser (Recommended)

### Windows/Linux
- **Chrome/Edge**: `Ctrl + Shift + R` or `Ctrl + F5`
- **Firefox**: `Ctrl + Shift + R` or `Ctrl + F5`

### Mac
- **Chrome/Edge/Safari**: `Cmd + Shift + R`
- **Firefox**: `Cmd + Shift + R`

This clears the cached CSS and JavaScript files.

---

## Solution 2: Clear Browser Cache

### Chrome/Edge
1. Press `Ctrl + Shift + Delete` (Windows) or `Cmd + Shift + Delete` (Mac)
2. Select "Cached images and files"
3. Choose "All time"
4. Click "Clear data"

### Firefox
1. Press `Ctrl + Shift + Delete` (Windows) or `Cmd + Shift + Delete` (Mac)
2. Select "Cache"
3. Choose "Everything"
4. Click "Clear Now"

### Safari
1. Go to Safari → Preferences → Advanced
2. Check "Show Develop menu in menu bar"
3. Go to Develop → Empty Caches
4. Or press `Cmd + Option + E`

---

## Solution 3: Restart Django Server

1. Stop the server: `Ctrl + C`
2. Start it again:
   ```bash
   cd healthcare_chatbot_project
   python manage.py runserver
   ```
3. Hard refresh your browser

---

## Solution 4: Open in Incognito/Private Mode

This bypasses all cache:

- **Chrome/Edge**: `Ctrl + Shift + N` (Windows) or `Cmd + Shift + N` (Mac)
- **Firefox**: `Ctrl + Shift + P` (Windows) or `Cmd + Shift + P` (Mac)
- **Safari**: `Cmd + Shift + N`

Then navigate to `http://127.0.0.1:8000/`

---

## Solution 5: Check File Versions

The HTML template now includes version numbers:
```html
<link rel="stylesheet" href="/static/styles.css?v=2.0">
<script src="/static/chat.js?v=2.0"></script>
```

If you don't see `?v=2.0` in the browser's Network tab, the HTML wasn't updated.

---

## Solution 6: Verify Files Are Updated

### Check CSS Variables
Open `healthcare_chatbot_project/static/styles.css` and verify the first lines show:

```css
:root {
  --dark-bg-primary: #0d1117;
  --dark-bg-secondary: #161b22;
  --dark-bg-tertiary: #1c2128;
  --dark-accent-primary: #58a6ff;
  ...
}
```

If you see `#0a0e27` or `#667eea`, the file wasn't updated.

### Check HTML Template
Open `healthcare_chatbot_project/templates/chat/index.html` and verify it includes:
```html
<link rel="stylesheet" href="/static/styles.css?v=2.0">
```

---

## Solution 7: Check Browser Console

1. Open Developer Tools: `F12` or `Ctrl + Shift + I`
2. Go to "Console" tab
3. Look for any errors (red text)
4. Go to "Network" tab
5. Refresh the page
6. Check if `styles.css` loads successfully (status 200)

---

## Solution 8: Disable Browser Extensions

Some extensions can interfere with CSS:
1. Open browser in Incognito/Private mode (extensions disabled by default)
2. Or manually disable extensions temporarily
3. Refresh the page

---

## Solution 9: Check Django Static Files Settings

Open `healthcare_chatbot_project/healthcare/settings.py` and verify:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

---

## Solution 10: Manual File Check

1. Navigate to: `http://127.0.0.1:8000/static/styles.css`
2. You should see the CSS file content
3. Check if the first lines show the new colors:
   - `--dark-bg-primary: #0d1117;` ✅ New
   - `--dark-bg-primary: #0a0e27;` ❌ Old

---

## What You Should See (New UI)

### Colors
- **Background**: Dark gray (#0d1117), not purple-blue
- **Navbar**: Dark gray (#161b22), not purple
- **Buttons**: Blue (#58a6ff), not purple gradient
- **Text**: Light gray (#c9d1d9), not purple-tinted
- **Borders**: Subtle gray (#30363d), not glowing purple

### Effects
- ❌ No gradient backgrounds
- ❌ No floating particles
- ❌ No shimmer effects
- ❌ No glow effects
- ✅ Clean, solid colors
- ✅ Minimal shadows
- ✅ Professional look

---

## Still Not Working?

### Check File Paths
Verify these files exist:
```
healthcare_chatbot_project/
├── static/
│   ├── styles.css  ← Should have new colors
│   └── chat.js
├── templates/
│   └── chat/
│       └── index.html  ← Should have ?v=2.0
└── manage.py
```

### Check Django is Running
```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### Check URL
Make sure you're visiting:
```
http://127.0.0.1:8000/
```

Not:
- `http://localhost:8000/` (might have different cache)
- `file:///...` (opening HTML directly)

---

## Quick Test

Open browser console and run:
```javascript
getComputedStyle(document.body).backgroundColor
```

**Expected result**: `rgb(13, 17, 23)` (which is #0d1117)
**Old result**: `rgb(10, 14, 39)` (which is #0a0e27)

---

## Force Update Script

If nothing works, create this file:

**clear_cache.html** (in healthcare_chatbot_project folder)
```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <script>
        // Clear cache and redirect
        if ('caches' in window) {
            caches.keys().then(names => {
                names.forEach(name => caches.delete(name));
            });
        }
        setTimeout(() => {
            window.location.href = 'http://127.0.0.1:8000/';
        }, 1000);
    </script>
</head>
<body>
    <h1>Clearing cache...</h1>
    <p>Redirecting to chatbot...</p>
</body>
</html>
```

Open this file in your browser, then it will redirect to the chatbot with cleared cache.

---

## Contact Info

If you've tried all solutions and it still doesn't work:

1. Check the browser console for errors
2. Verify the CSS file content directly
3. Try a different browser
4. Restart your computer (clears all caches)

---

## Success Checklist

✅ Hard refreshed browser (Ctrl+Shift+R)
✅ Cleared browser cache
✅ Restarted Django server
✅ Tried incognito mode
✅ Verified CSS file has new colors
✅ Checked browser console for errors
✅ Visited correct URL (127.0.0.1:8000)
✅ Disabled browser extensions

If all checked, you should see the new dark mode! 🌙
