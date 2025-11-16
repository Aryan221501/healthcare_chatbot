# 🧪 Testing the Medical Knowledge Base

## Quick Test Queries

### 1. **Greetings**
Try: `hello`, `hi`, `hey`
Expected: Welcome message with instructions

### 2. **Help**
Try: `help`
Expected: List of available topics and example questions

### 3. **Common Cold**
Try: 
- `I have a cold`
- `runny nose and sneezing`
- `I'm congested`

Expected: Detailed cold information

### 4. **Flu**
Try:
- `I have the flu`
- `body aches and chills`
- `influenza symptoms`

Expected: Comprehensive flu information

### 5. **Fever**
Try:
- `I have a fever`
- `my temperature is high`
- `I'm feverish`

Expected: Fever ranges, treatment, when to see doctor

### 6. **Cough**
Try:
- `I have a cough`
- `persistent coughing`
- `dry cough`

Expected: Cough types, causes, treatment

### 7. **Headache**
Try:
- `I have a headache`
- `my head hurts`
- `migraine`

Expected: Headache types, triggers, treatment

### 8. **Stomach Issues**
Try:
- `stomach ache`
- `nausea and vomiting`
- `diarrhea`

Expected: Digestive issues information

### 9. **Allergies**
Try:
- `I have allergies`
- `itchy eyes and sneezing`
- `allergic reaction`

Expected: Allergy types, treatment, anaphylaxis info

### 10. **Diabetes**
Try:
- `what is diabetes?`
- `blood sugar problems`
- `diabetic symptoms`

Expected: Diabetes types, management, complications

### 11. **High Blood Pressure**
Try:
- `high blood pressure`
- `hypertension`
- `my BP is high`

Expected: BP ranges, management, prevention

### 12. **Asthma**
Try:
- `I have asthma`
- `wheezing and shortness of breath`
- `breathing difficulty`

Expected: Asthma symptoms, triggers, management

### 13. **Heart Disease**
Try:
- `heart problems`
- `chest pain`
- `heart attack symptoms`

Expected: Heart disease info + emergency warning

### 14. **Mental Health**
Try:
- `I'm feeling depressed`
- `anxiety and stress`
- `mental health help`

Expected: Mental health info with crisis resources

### 15. **COVID-19**
Try:
- `COVID symptoms`
- `coronavirus`
- `COVID-19 prevention`

Expected: COVID information, testing, isolation

### 16. **General Health**
Try:
- `how to stay healthy`
- `wellness tips`
- `preventive care`

Expected: General health and wellness information

### 17. **Emergency (IMPORTANT)**
Try:
- `I have severe chest pain`
- `I can't breathe`
- `heart attack`

Expected: 🚨 EMERGENCY RESPONSE with 911 instructions

---

## Expected Response Format

Each response should include:
- ✅ Clear heading with emoji
- ✅ Symptoms section
- ✅ Treatment section
- ✅ "When to see a doctor" section
- ✅ Prevention tips (where applicable)
- ✅ Emergency signs (where applicable)

---

## Testing Checklist

- [ ] Greetings work
- [ ] Help command works
- [ ] At least 5 different conditions tested
- [ ] Emergency detection works
- [ ] Responses are detailed and formatted
- [ ] "When to see doctor" included
- [ ] No errors in console
- [ ] Responses appear quickly (1-2 seconds)

---

## What to Check

### ✅ Good Response:
- Detailed information
- Well-formatted with bullets
- Includes symptoms, treatment, when to seek help
- Clear and easy to read
- Appropriate emoji

### ❌ Bad Response:
- Generic "I don't understand"
- No formatting
- Too short or vague
- Missing important information

---

## Troubleshooting

### If responses are generic:
1. Check if `medical_kb.py` is in the `chat` folder
2. Restart Django server
3. Hard refresh browser (Ctrl+Shift+R)

### If emergency detection doesn't work:
1. Try exact phrases: "chest pain", "can't breathe"
2. Check console for errors
3. Verify EMERGENCY_KEYWORDS in medical_kb.py

### If no response at all:
1. Check server is running
2. Check browser console for errors
3. See QUICK_FIX.md

---

## Success Criteria

✅ **Comprehensive responses** for all major conditions
✅ **Emergency detection** works immediately
✅ **Clear formatting** with sections and bullets
✅ **Helpful guidance** on when to seek care
✅ **Fast responses** (1-2 seconds)
✅ **No errors** in console or server

---

## Example Test Session

```
User: hello
Bot: Welcome message with instructions ✅

User: I have a fever and cough
Bot: Detailed fever information ✅

User: what is diabetes?
Bot: Comprehensive diabetes information ✅

User: I have chest pain
Bot: 🚨 EMERGENCY RESPONSE with 911 ✅

User: help
Bot: List of topics and examples ✅
```

---

## Quick Test Script

Copy and paste these one by one:

```
hello
help
I have a fever
I have a cough
I have a headache
stomach ache
what is diabetes?
high blood pressure
I'm feeling anxious
COVID symptoms
I have chest pain
```

Each should return a detailed, well-formatted response!

---

## Performance Metrics

- **Response time:** < 2 seconds
- **Accuracy:** Matches correct condition
- **Completeness:** Includes all sections
- **Clarity:** Easy to understand
- **Safety:** Emergency detection works

---

## Report Issues

If you find:
- Missing information
- Incorrect medical advice
- Formatting issues
- Emergency detection failures
- Slow responses

Check:
1. Server logs for errors
2. Browser console for errors
3. medical_kb.py for typos
4. views.py for logic errors

---

**Happy Testing! 🧪**
