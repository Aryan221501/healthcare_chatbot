# 🧪 Testing the Diagnosis System

## Quick Test Scenarios

### Test 1: Start Diagnosis
```
Type: diagnose
Expected: Welcome message with instructions
```

### Test 2: Flu Diagnosis
```
1. Type: I have a cough and fever
2. Bot asks: Do you have a fever?
3. Answer: yes
4. Bot asks: Are you experiencing severe body aches?
5. Answer: yes
6. Result: Flu diagnosis with detailed information
```

### Test 3: Cold Diagnosis
```
1. Type: diagnose respiratory
2. Bot asks: Do you have a fever?
3. Answer: no
4. Bot asks: Do you have a runny or stuffy nose?
5. Answer: yes
6. Bot asks: Are you sneezing frequently?
7. Answer: yes
8. Result: Common Cold diagnosis
```

### Test 4: Stomach Issues
```
1. Type: my stomach hurts
2. Bot asks: Do you have a fever?
3. Answer: no
4. Bot asks: Is the pain in your upper abdomen?
5. Answer: yes
6. Bot asks: Does the pain worsen after eating?
7. Answer: yes
8. Result: Indigestion diagnosis
```

### Test 5: Emergency Detection (Appendicitis)
```
1. Type: diagnose digestive
2. Bot asks: Do you have a fever?
3. Answer: yes
4. Bot asks: Are you experiencing diarrhea?
5. Answer: no
6. Bot asks: Is the pain severe and localized to lower right abdomen?
7. Answer: yes
8. Result: 🚨 URGENT - Possible Appendicitis with ER instructions
```

### Test 6: Cancel Diagnosis
```
1. Type: diagnose
2. Bot asks question
3. Type: cancel
4. Result: Diagnosis cancelled message
```

### Test 7: Invalid Answer
```
1. Type: diagnose
2. Bot asks: Do you have a fever?
3. Type: maybe
4. Result: "Please answer with yes or no"
```

### Test 8: Allergies Diagnosis
```
1. Type: I'm sneezing a lot
2. Answer: no (fever)
3. Answer: yes (runny nose)
4. Answer: no (sneezing frequently)
5. Answer: yes (itchy eyes)
6. Result: Allergic Rhinitis diagnosis
```

---

## What to Check

### ✅ Diagnosis Flow:
- [ ] Diagnosis starts correctly
- [ ] Questions appear one at a time
- [ ] Yes/no answers work
- [ ] Questions follow logical path
- [ ] Final diagnosis appears
- [ ] Diagnosis is detailed and formatted

### ✅ User Experience:
- [ ] Clear instructions
- [ ] Question numbers shown
- [ ] Can cancel anytime
- [ ] Invalid answers handled gracefully
- [ ] Session persists across messages
- [ ] Session clears after diagnosis

### ✅ Content Quality:
- [ ] Diagnoses are accurate
- [ ] Recommendations are helpful
- [ ] Emergency conditions flagged
- [ ] Disclaimers included
- [ ] "When to see doctor" included

### ✅ Edge Cases:
- [ ] Typing "yes" vs "y" vs "yeah" works
- [ ] Typing "no" vs "n" vs "nope" works
- [ ] Cancel works at any point
- [ ] Invalid input handled
- [ ] Multiple diagnosis sessions work

---

## Expected Behavior

### Starting Diagnosis:
**Input:** "diagnose" or "I have a cough"
**Output:** 
- Welcome message
- First question
- Instructions to answer yes/no

### During Diagnosis:
**Input:** "yes" or "no"
**Output:**
- Next question with number
- Or final diagnosis if complete

### Completing Diagnosis:
**Output:**
- Emoji based on severity
- Condition name
- Detailed description
- Treatment recommendations
- When to seek care
- Confidence level
- Disclaimer

### Canceling:
**Input:** "cancel"
**Output:** "Diagnosis cancelled" message

---

## Common Issues & Solutions

### Issue: Diagnosis doesn't start
**Check:**
- Is server running?
- Did you type "diagnose" or describe symptoms?
- Check console for errors

### Issue: Questions don't progress
**Check:**
- Are you answering "yes" or "no"?
- Check if session is stored
- Restart server if needed

### Issue: Diagnosis incomplete
**Check:**
- Did you answer all questions?
- Check diagnosis_engine.py for tree structure
- Verify all paths lead to diagnosis

### Issue: Same question repeats
**Check:**
- Session management
- Question ID mapping
- Answer parsing

---

## Performance Metrics

### Response Time:
- Question display: < 1 second
- Diagnosis generation: < 2 seconds

### Accuracy:
- Questions should logically follow answers
- Diagnosis should match symptom pattern
- Emergency conditions should be flagged

### User Experience:
- Clear, easy to understand
- Minimal typing required
- Fast and responsive
- Professional appearance

---

## Success Criteria

✅ **All test scenarios pass**
✅ **Questions flow logically**
✅ **Diagnoses are accurate and detailed**
✅ **Emergency conditions flagged appropriately**
✅ **User can cancel anytime**
✅ **Invalid inputs handled gracefully**
✅ **Session management works correctly**
✅ **No errors in console**

---

## Quick Test Commands

Copy and paste these to test quickly:

```
# Test 1: Flu
diagnose
yes
yes

# Test 2: Cold
diagnose
no
yes
yes

# Test 3: Cancel
diagnose
cancel

# Test 4: Stomach
my stomach hurts
no
yes
yes

# Test 5: Emergency
diagnose digestive
yes
no
yes
```

---

## Debugging

### Check Server Logs:
Look for:
- Session creation
- Question progression
- Diagnosis completion
- Any errors

### Check Browser Console:
Look for:
- API responses
- Session ID
- Any JavaScript errors

### Check diagnosis_sessions:
In views.py, add print statements:
```python
print(f"Session: {session}")
print(f"Diagnosis sessions: {diagnosis_sessions}")
```

---

**Happy Testing! 🧪**

If all tests pass, your diagnosis system is working perfectly! 🎉
