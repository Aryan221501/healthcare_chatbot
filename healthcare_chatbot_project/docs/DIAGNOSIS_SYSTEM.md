# 🔍 Interactive Diagnosis System

## Overview
The chatbot now includes an interactive diagnosis feature that asks yes/no questions to help identify medical conditions.

---

## 🎯 How It Works

### 1. **User Initiates Diagnosis**
User can start diagnosis by:
- Typing "diagnose"
- Typing "check my symptoms"
- Typing "diagnosis"
- Describing symptoms (e.g., "I have a cough")

### 2. **System Asks Questions**
- Bot asks a series of yes/no questions
- Questions are tailored based on previous answers
- Decision tree narrows down possible conditions

### 3. **Final Diagnosis**
- After 3-8 questions, bot provides diagnosis
- Includes detailed information about the condition
- Provides treatment recommendations
- Indicates when to seek medical care

---

## 📋 Available Diagnosis Categories

### 1. **Respiratory Issues**
Diagnoses conditions like:
- Common Cold
- Influenza (Flu)
- Acute Bronchitis
- Asthma Attack
- Allergic Rhinitis
- Persistent Dry Cough
- Viral Upper Respiratory Infection

**Triggers:** cough, breathing, throat, chest, congestion, sneeze

### 2. **Digestive Issues**
Diagnoses conditions like:
- Gastroenteritis (Stomach Flu)
- Appendicitis (Emergency)
- Indigestion
- Constipation
- GERD (Acid Reflux)
- Gastritis
- IBS (Irritable Bowel Syndrome)

**Triggers:** stomach, nausea, vomit, diarrhea, abdominal, belly

---

## 💬 Example Diagnosis Session

### Respiratory Diagnosis Example:

```
User: I have a cough and feel sick

Bot: 🔍 Starting Interactive Diagnosis

I'll ask you a series of yes/no questions to help identify your condition.

Please answer with "yes" or "no"

Question 1:
Do you have a fever (temperature above 100.4°F/38°C)?

Type "yes" or "no" to continue.

---

User: yes

Bot: Question 2:
Are you experiencing severe body aches and fatigue?

Type "yes" or "no" to continue.

---

User: yes

Bot: 🤒 Diagnosis Complete

Likely Diagnosis: Influenza (Flu)

Based on your symptoms:
• Fever (>100.4°F/38°C)
• Severe body aches and fatigue
• Respiratory symptoms

Recommended Actions:
1. Rest: Stay home for at least 24 hours after fever subsides
2. Hydrate: Drink plenty of fluids
3. Medication: Take acetaminophen or ibuprofen
4. Antiviral: Contact doctor within 48 hours

[Full detailed information...]

Confidence Level: High
```

---

## 🎮 User Commands

### Start Diagnosis:
- `diagnose`
- `check my symptoms`
- `diagnosis`
- `I have a cough` (automatic detection)

### During Diagnosis:
- `yes` / `y` / `yeah` / `yep` / `yup` - Answer yes
- `no` / `n` / `nope` / `nah` - Answer no
- `cancel` / `stop` / `quit` / `exit` - Cancel diagnosis

---

## 🌳 Decision Tree Logic

### Respiratory Tree Example:
```
Q1: Do you have a fever?
├─ Yes → Q2: Severe body aches?
│         ├─ Yes → DIAGNOSIS: Flu
│         └─ No → Q4: Thick mucus?
│                  ├─ Yes → DIAGNOSIS: Bronchitis
│                  └─ No → DIAGNOSIS: Viral Infection
└─ No → Q3: Runny nose?
        ├─ Yes → Q5: Sneezing?
        │        ├─ Yes → DIAGNOSIS: Cold
        │        └─ No → Q7: Itchy eyes?
        │                 ├─ Yes → DIAGNOSIS: Allergies
        │                 └─ No → DIAGNOSIS: Cold
        └─ No → Q6: Difficulty breathing?
                ├─ Yes → DIAGNOSIS: Asthma
                └─ No → Q8: Dry cough?
                         ├─ Yes → DIAGNOSIS: Dry Cough
                         └─ No → DIAGNOSIS: General Respiratory
```

---

## 📊 Diagnosis Output Format

Each diagnosis includes:

### ✅ Condition Name
Clear identification of the likely condition

### ✅ Confidence Level
- High: Strong match with symptoms
- Moderate: Likely match, but see doctor
- Low: Unclear, professional evaluation needed

### ✅ Based on Your Symptoms
Summary of key symptoms that led to diagnosis

### ✅ Recommended Actions
1. Immediate steps to take
2. Home remedies
3. Medications (OTC)
4. Lifestyle changes

### ✅ When to See a Doctor
Clear guidelines on when professional care is needed

### ✅ When to Seek Emergency Care
Life-threatening symptoms requiring immediate attention

### ✅ Duration/Recovery Time
Expected timeline for recovery

### ✅ Prevention Tips
How to avoid condition in future

---

## 🚨 Emergency Detection

If diagnosis indicates emergency (e.g., Appendicitis):
- Marked with 🚨 URGENT or EMERGENCY
- Clear instructions to call 911 or go to ER
- What NOT to do while waiting
- Why it's urgent

---

## 🔒 Safety Features

### 1. **Disclaimers**
Every diagnosis includes:
> "This is an automated assessment. It is NOT a substitute for professional medical advice."

### 2. **Professional Guidance**
Always recommends seeing healthcare provider when:
- Symptoms are severe
- Diagnosis is unclear
- Condition requires prescription medication
- Emergency signs present

### 3. **Confidence Levels**
- High: Strong symptom match
- Moderate: Possible match, verify with doctor
- Low: Unclear, needs professional evaluation

### 4. **Emergency Prioritization**
Conditions like appendicitis trigger immediate emergency response

---

## 💾 Session Management

### How Sessions Work:
1. User starts diagnosis → Session created
2. Each answer stored in session
3. Session guides through decision tree
4. After diagnosis → Session deleted
5. User can start new diagnosis anytime

### Session Data Stored:
```python
{
    'category': 'respiratory',
    'current_question': 'q2',
    'answers': [
        {'question_id': 'q1', 'answer': True},
        {'question_id': 'q2', 'answer': True}
    ]
}
```

---

## 🎯 Accuracy & Limitations

### Strengths:
✅ Systematic symptom evaluation
✅ Evidence-based decision trees
✅ Clear, actionable recommendations
✅ Appropriate urgency levels

### Limitations:
❌ Cannot replace physical examination
❌ Cannot order tests or see results
❌ Cannot prescribe medications
❌ Limited to common conditions
❌ Requires honest, accurate answers

### Best Used For:
- Understanding possible conditions
- Knowing when to seek care
- Getting initial guidance
- Learning about symptoms

### NOT a Substitute For:
- Doctor visits
- Emergency care
- Diagnostic tests
- Professional medical advice

---

## 🔮 Future Enhancements

Potential additions:
- More diagnosis categories (headaches, skin conditions, etc.)
- Symptom severity scales (1-10)
- Multiple condition possibilities
- Symptom duration tracking
- Follow-up questions based on age/gender
- Integration with telemedicine
- Appointment booking
- Medication interaction checker

---

## 📝 Example Use Cases

### Use Case 1: Cold vs Flu
**Problem:** User unsure if they have cold or flu
**Solution:** Diagnosis asks about fever, body aches, severity
**Result:** Accurate identification and appropriate treatment

### Use Case 2: Stomach Pain
**Problem:** User has abdominal pain, unsure if serious
**Solution:** Diagnosis asks about location, fever, severity
**Result:** Identifies if emergency (appendicitis) or manageable (indigestion)

### Use Case 3: Breathing Issues
**Problem:** User having breathing difficulty
**Solution:** Diagnosis determines if asthma, allergies, or infection
**Result:** Appropriate urgency level and treatment guidance

---

## 🧪 Testing the Diagnosis System

### Test Scenario 1: Flu Diagnosis
```
1. Type: "I feel sick"
2. Answer: yes (fever)
3. Answer: yes (body aches)
4. Result: Flu diagnosis with treatment plan
```

### Test Scenario 2: Cold Diagnosis
```
1. Type: "diagnose"
2. Describe: "runny nose"
3. Answer: no (fever)
4. Answer: yes (runny nose)
5. Answer: yes (sneezing)
6. Result: Cold diagnosis
```

### Test Scenario 3: Emergency Detection
```
1. Type: "stomach pain"
2. Answer: yes (fever)
3. Answer: no (diarrhea)
4. Answer: yes (lower right abdomen)
5. Result: 🚨 URGENT - Possible Appendicitis
```

### Test Scenario 4: Cancel Diagnosis
```
1. Type: "diagnose"
2. Answer: yes
3. Type: "cancel"
4. Result: Diagnosis cancelled
```

---

## 📊 Statistics

### Coverage:
- **2 diagnosis categories** (Respiratory, Digestive)
- **15+ possible diagnoses**
- **3-8 questions** per diagnosis
- **Average time:** 2-3 minutes

### Accuracy Factors:
- Honest answers from user
- Clear symptom description
- Appropriate category selection
- Understanding of questions

---

## ⚠️ Important Notes

### This System:
✅ Provides educational information
✅ Helps understand symptoms
✅ Guides when to seek care
✅ Offers initial assessment

### This System Does NOT:
❌ Replace doctor visits
❌ Provide definitive diagnosis
❌ Prescribe medications
❌ Guarantee accuracy
❌ Handle all conditions

### Always:
🏥 Consult healthcare professionals for medical decisions
🚨 Call 911 for emergencies
💊 Follow prescribed treatment plans
📅 Keep regular checkups

---

## 🎉 Summary

The Interactive Diagnosis System provides:
- **Systematic symptom evaluation** through yes/no questions
- **Evidence-based diagnoses** for common conditions
- **Detailed treatment recommendations**
- **Clear guidance** on when to seek professional care
- **Emergency detection** for serious conditions
- **User-friendly interface** with simple yes/no answers

**Perfect for:** Initial symptom assessment, understanding conditions, and knowing when to seek professional medical care.

**Remember:** This is an educational tool. Always consult healthcare professionals for medical advice! 🏥
