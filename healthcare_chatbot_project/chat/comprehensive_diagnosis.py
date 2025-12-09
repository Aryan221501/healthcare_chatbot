# Comprehensive Diagnosis Engine with Multiple Disease Categories

__all__ = ['COMPREHENSIVE_DIAGNOSIS_TREES', 'get_comprehensive_diagnosis_category']

COMPREHENSIVE_DIAGNOSIS_TREES = {
    'cardiovascular': {
        'name': 'Cardiovascular Issues',
        'initial_symptoms': ['chest pain', 'heart', 'palpitation', 'irregular heartbeat', 'chest pressure', 'angina'],
        'questions': [
            {'id': 'q1', 'question': 'Are you experiencing severe chest pain or pressure?', 'yes': 'diagnosis_emergency_heart', 'no': 'q2'},
            {'id': 'q2', 'question': 'Do you have irregular or rapid heartbeat?', 'yes': 'q3', 'no': 'q4'},
            {'id': 'q3', 'question': 'Are you feeling dizzy or lightheaded?', 'yes': 'diagnosis_arrhythmia', 'no': 'diagnosis_palpitations'},
            {'id': 'q4', 'question': 'Do you have shortness of breath?', 'yes': 'diagnosis_heart_failure', 'no': 'diagnosis_general_cardio'}
        ],
        'diagnoses': {
            'diagnosis_emergency_heart': {
                'condition': 'Possible Heart Attack',
                'confidence': 'Emergency',
                'description': '🚨 **MEDICAL EMERGENCY: Possible Heart Attack**\n\n**CALL 911 IMMEDIATELY!**\n\n**While waiting:**\n1. Sit down and stay calm\n2. Chew aspirin if available (unless allergic)\n3. Loosen tight clothing\n4. Do NOT drive yourself\n\n**This is a life-threatening emergency!**',
                'severity': 'emergency'
            },
            'diagnosis_arrhythmia': {
                'condition': 'Cardiac Arrhythmia',
                'confidence': 'Moderate',
                'description': '💓 **Possible Diagnosis: Cardiac Arrhythmia**\n\n**Symptoms:** Irregular heartbeat, dizziness, lightheadedness\n\n**Recommended Actions:**\n1. See a cardiologist immediately\n2. Get an ECG/EKG test\n3. Monitor your heart rate\n4. Avoid caffeine and stimulants\n\n**When to seek emergency care:** Chest pain, fainting, severe shortness of breath',
                'severity': 'high'
            },
            'diagnosis_palpitations': {
                'condition': 'Heart Palpitations',
                'confidence': 'Moderate',
                'description': '💗 **Likely Diagnosis: Heart Palpitations**\n\n**Common Causes:** Stress, anxiety, caffeine, dehydration\n\n**Recommended Actions:**\n1. Reduce caffeine and alcohol\n2. Manage stress (meditation, yoga)\n3. Stay hydrated\n4. Get adequate sleep\n5. See doctor if persistent\n\n**When to see a doctor:** Frequent episodes, chest pain, fainting',
                'severity': 'mild'
            },
            'diagnosis_heart_failure': {
                'condition': 'Possible Heart Failure',
                'confidence': 'High',
                'description': '🫀 **Possible Diagnosis: Heart Failure**\n\n**Symptoms:** Shortness of breath, fatigue, swelling\n\n**URGENT: See a cardiologist immediately**\n\n**Recommended Actions:**\n1. Schedule urgent cardiology appointment\n2. Limit salt intake\n3. Monitor fluid intake\n4. Rest frequently\n\n**Emergency signs:** Severe breathing difficulty, chest pain, coughing up blood',
                'severity': 'high'
            },
            'diagnosis_general_cardio': {
                'condition': 'General Cardiovascular Concern',
                'confidence': 'Low',
                'description': '🏥 **Recommendation: Cardiology Consultation**\n\nYour symptoms need professional evaluation. Please schedule an appointment with a cardiologist.\n\n**Seek immediate care if:** Chest pain, severe shortness of breath, fainting',
                'severity': 'moderate'
            }
        }
    },
    
    'neurological': {
        'name': 'Neurological Issues',
        'initial_symptoms': ['headache', 'migraine', 'dizziness', 'vertigo', 'seizure', 'numbness', 'tingling'],
        'questions': [
            {'id': 'q1', 'question': 'Is this the worst headache of your life?', 'yes': 'diagnosis_emergency_neuro', 'no': 'q2'},
            {'id': 'q2', 'question': 'Do you have nausea, vomiting, or sensitivity to light?', 'yes': 'q3', 'no': 'q4'},
            {'id': 'q3', 'question': 'Is the pain on one side of your head?', 'yes': 'diagnosis_migraine', 'no': 'diagnosis_tension_headache'},
            {'id': 'q4', 'question': 'Do you have numbness or tingling in your limbs?', 'yes': 'diagnosis_neuropathy', 'no': 'q5'},
            {'id': 'q5', 'question': 'Are you experiencing dizziness or vertigo?', 'yes': 'diagnosis_vertigo', 'no': 'diagnosis_general_neuro'}
        ],
        'diagnoses': {
            'diagnosis_emergency_neuro': {
                'condition': 'Possible Stroke or Brain Emergency',
                'confidence': 'Emergency',
                'description': '🚨 **MEDICAL EMERGENCY**\n\n**CALL 911 IMMEDIATELY!**\n\n**Signs of stroke (FAST):**\n- **F**ace drooping\n- **A**rm weakness\n- **S**peech difficulty\n- **T**ime to call 911\n\n**Do NOT wait! Every minute counts!**',
                'severity': 'emergency'
            },
            'diagnosis_migraine': {
                'condition': 'Migraine Headache',
                'confidence': 'High',
                'description': '🤕 **Likely Diagnosis: Migraine**\n\n**Symptoms:** One-sided headache, nausea, light sensitivity\n\n**Recommended Actions:**\n1. Rest in dark, quiet room\n2. Take prescribed migraine medication\n3. Apply cold compress\n4. Stay hydrated\n5. Avoid triggers (stress, certain foods)\n\n**When to see a doctor:** Frequent migraines, new symptoms, medication not helping',
                'severity': 'moderate'
            },
            'diagnosis_tension_headache': {
                'condition': 'Tension Headache',
                'confidence': 'High',
                'description': '😣 **Likely Diagnosis: Tension Headache**\n\n**Symptoms:** Band-like pressure, both sides of head\n\n**Recommended Actions:**\n1. Take OTC pain reliever (ibuprofen, acetaminophen)\n2. Apply heat or cold pack\n3. Massage neck and shoulders\n4. Practice relaxation techniques\n5. Improve posture\n\n**Prevention:** Manage stress, regular exercise, adequate sleep',
                'severity': 'mild'
            },
            'diagnosis_neuropathy': {
                'condition': 'Peripheral Neuropathy',
                'confidence': 'Moderate',
                'description': '🦵 **Possible Diagnosis: Peripheral Neuropathy**\n\n**Symptoms:** Numbness, tingling, burning sensation\n\n**Recommended Actions:**\n1. See a neurologist\n2. Check blood sugar levels (diabetes screening)\n3. Vitamin B12 supplementation\n4. Avoid alcohol\n\n**Common causes:** Diabetes, vitamin deficiency, nerve compression',
                'severity': 'moderate'
            },
            'diagnosis_vertigo': {
                'condition': 'Vertigo/Balance Disorder',
                'confidence': 'Moderate',
                'description': '🌀 **Likely Diagnosis: Vertigo**\n\n**Symptoms:** Spinning sensation, dizziness, balance problems\n\n**Recommended Actions:**\n1. Sit or lie down immediately\n2. Avoid sudden movements\n3. Stay hydrated\n4. See an ENT specialist\n5. Try Epley maneuver (if BPPV)\n\n**When to seek emergency care:** Severe headache, double vision, difficulty speaking',
                'severity': 'moderate'
            },
            'diagnosis_general_neuro': {
                'condition': 'General Neurological Concern',
                'confidence': 'Low',
                'description': '🧠 **Recommendation: Neurological Evaluation**\n\nYour symptoms need professional assessment. Please see a neurologist.\n\n**Seek immediate care if:** Sudden severe symptoms, loss of consciousness, seizures',
                'severity': 'moderate'
            }
        }
    },
    
    'dermatological': {
        'name': 'Skin Issues',
        'initial_symptoms': ['rash', 'itching', 'skin', 'acne', 'eczema', 'psoriasis', 'hives'],
        'questions': [
            {'id': 'q1', 'question': 'Is the rash spreading rapidly or accompanied by difficulty breathing?', 'yes': 'diagnosis_emergency_allergic', 'no': 'q2'},
            {'id': 'q2', 'question': 'Is the affected area red, itchy, and inflamed?', 'yes': 'q3', 'no': 'q4'},
            {'id': 'q3', 'question': 'Does it appear in patches or specific areas?', 'yes': 'diagnosis_eczema', 'no': 'diagnosis_contact_dermatitis'},
            {'id': 'q4', 'question': 'Do you have raised, scaly patches?', 'yes': 'diagnosis_psoriasis', 'no': 'q5'},
            {'id': 'q5', 'question': 'Are there pimples or blackheads?', 'yes': 'diagnosis_acne', 'no': 'diagnosis_general_derm'}
        ],
        'diagnoses': {
            'diagnosis_emergency_allergic': {
                'condition': 'Severe Allergic Reaction',
                'confidence': 'Emergency',
                'description': '🚨 **MEDICAL EMERGENCY: Anaphylaxis**\n\n**CALL 911 IMMEDIATELY!**\n\n**If you have an EpiPen, use it now!**\n\n**Signs of anaphylaxis:**\n- Difficulty breathing\n- Swelling of face/throat\n- Rapid pulse\n- Dizziness\n\n**This is life-threatening!**',
                'severity': 'emergency'
            },
            'diagnosis_eczema': {
                'condition': 'Eczema (Atopic Dermatitis)',
                'confidence': 'High',
                'description': '🧴 **Likely Diagnosis: Eczema**\n\n**Symptoms:** Red, itchy, inflamed patches\n\n**Recommended Actions:**\n1. Moisturize frequently (fragrance-free)\n2. Use gentle, hypoallergenic products\n3. Apply hydrocortisone cream\n4. Avoid triggers (harsh soaps, stress)\n5. Take lukewarm baths\n\n**When to see a dermatologist:** Severe symptoms, infection, not improving',
                'severity': 'mild'
            },
            'diagnosis_contact_dermatitis': {
                'condition': 'Contact Dermatitis',
                'confidence': 'High',
                'description': '🌿 **Likely Diagnosis: Contact Dermatitis**\n\n**Cause:** Reaction to irritant or allergen\n\n**Recommended Actions:**\n1. Identify and avoid trigger\n2. Wash affected area gently\n3. Apply cool compress\n4. Use hydrocortisone cream\n5. Take antihistamine for itching\n\n**Common triggers:** Poison ivy, nickel, fragrances, latex',
                'severity': 'mild'
            },
            'diagnosis_psoriasis': {
                'condition': 'Psoriasis',
                'confidence': 'Moderate',
                'description': '🔴 **Possible Diagnosis: Psoriasis**\n\n**Symptoms:** Raised, scaly, red patches\n\n**Recommended Actions:**\n1. See a dermatologist for diagnosis\n2. Moisturize regularly\n3. Use prescribed topical treatments\n4. Get sunlight (moderate amounts)\n5. Manage stress\n\n**Treatment options:** Topical creams, phototherapy, systemic medications',
                'severity': 'moderate'
            },
            'diagnosis_acne': {
                'condition': 'Acne Vulgaris',
                'confidence': 'High',
                'description': '😊 **Likely Diagnosis: Acne**\n\n**Recommended Actions:**\n1. Wash face twice daily (gentle cleanser)\n2. Use benzoyl peroxide or salicylic acid\n3. Don\'t pick or squeeze pimples\n4. Use oil-free, non-comedogenic products\n5. See dermatologist if severe\n\n**Treatment options:** Topical treatments, oral medications, lifestyle changes',
                'severity': 'mild'
            },
            'diagnosis_general_derm': {
                'condition': 'General Skin Condition',
                'confidence': 'Low',
                'description': '🏥 **Recommendation: Dermatology Consultation**\n\nYour skin condition needs professional evaluation. Please see a dermatologist.\n\n**Seek immediate care if:** Signs of infection, severe pain, rapid spreading',
                'severity': 'mild'
            }
        }
    },
    
    'mental_health': {
        'name': 'Mental Health',
        'initial_symptoms': ['anxiety', 'depression', 'stress', 'panic', 'sad', 'worried', 'mental health'],
        'questions': [
            {'id': 'q1', 'question': 'Are you having thoughts of harming yourself or others?', 'yes': 'diagnosis_emergency_mental', 'no': 'q2'},
            {'id': 'q2', 'question': 'Do you feel persistently sad or hopeless for more than 2 weeks?', 'yes': 'diagnosis_depression', 'no': 'q3'},
            {'id': 'q3', 'question': 'Do you experience sudden episodes of intense fear or panic?', 'yes': 'diagnosis_panic_disorder', 'no': 'q4'},
            {'id': 'q4', 'question': 'Do you worry excessively about everyday things?', 'yes': 'diagnosis_anxiety', 'no': 'diagnosis_stress'}
        ],
        'diagnoses': {
            'diagnosis_emergency_mental': {
                'condition': 'Mental Health Crisis',
                'confidence': 'Emergency',
                'description': '🚨 **IMMEDIATE HELP NEEDED**\n\n**Call 988 (Suicide & Crisis Lifeline) NOW**\n**Or call 911**\n\n**You are not alone. Help is available 24/7.**\n\n**Crisis Text Line:** Text HOME to 741741\n\n**Please reach out immediately. Your life matters!**',
                'severity': 'emergency'
            },
            'diagnosis_depression': {
                'condition': 'Major Depressive Disorder',
                'confidence': 'Moderate',
                'description': '💙 **Possible Diagnosis: Depression**\n\n**Symptoms:** Persistent sadness, hopelessness, loss of interest\n\n**Recommended Actions:**\n1. See a mental health professional immediately\n2. Talk to someone you trust\n3. Maintain routine and sleep schedule\n4. Exercise regularly\n5. Avoid alcohol and drugs\n\n**Treatment options:** Therapy (CBT), medication, lifestyle changes\n\n**You deserve support and can feel better!**',
                'severity': 'high'
            },
            'diagnosis_panic_disorder': {
                'condition': 'Panic Disorder',
                'confidence': 'Moderate',
                'description': '😰 **Possible Diagnosis: Panic Disorder**\n\n**Symptoms:** Sudden intense fear, rapid heartbeat, shortness of breath\n\n**Recommended Actions:**\n1. See a therapist or psychiatrist\n2. Practice deep breathing exercises\n3. Learn grounding techniques\n4. Avoid caffeine and stimulants\n5. Consider CBT therapy\n\n**During panic attack:** Breathe slowly, remind yourself it will pass, use 5-4-3-2-1 grounding',
                'severity': 'moderate'
            },
            'diagnosis_anxiety': {
                'condition': 'Generalized Anxiety Disorder',
                'confidence': 'Moderate',
                'description': '😟 **Possible Diagnosis: Anxiety Disorder**\n\n**Symptoms:** Excessive worry, restlessness, difficulty concentrating\n\n**Recommended Actions:**\n1. Consult a mental health professional\n2. Practice mindfulness and meditation\n3. Regular exercise\n4. Limit caffeine and alcohol\n5. Maintain healthy sleep habits\n\n**Treatment options:** Therapy, medication, relaxation techniques',
                'severity': 'moderate'
            },
            'diagnosis_stress': {
                'condition': 'Stress Response',
                'confidence': 'High',
                'description': '😓 **Likely Diagnosis: Stress**\n\n**Recommended Actions:**\n1. Identify stress sources\n2. Practice stress management (yoga, meditation)\n3. Exercise regularly\n4. Get adequate sleep\n5. Talk to friends/family\n6. Consider counseling if persistent\n\n**Self-care tips:** Take breaks, set boundaries, practice self-compassion',
                'severity': 'mild'
            }
        }
    },
    
    'musculoskeletal': {
        'name': 'Muscle and Joint Issues',
        'initial_symptoms': ['back pain', 'joint pain', 'muscle pain', 'arthritis', 'sprain', 'strain'],
        'questions': [
            {'id': 'q1', 'question': 'Did the pain start after an injury or accident?', 'yes': 'q2', 'no': 'q3'},
            {'id': 'q2', 'question': 'Is there visible swelling or deformity?', 'yes': 'diagnosis_fracture', 'no': 'diagnosis_sprain'},
            {'id': 'q3', 'question': 'Is the pain in your back?', 'yes': 'q4', 'no': 'q5'},
            {'id': 'q4', 'question': 'Does the pain radiate down your leg?', 'yes': 'diagnosis_sciatica', 'no': 'diagnosis_back_pain'},
            {'id': 'q5', 'question': 'Are multiple joints affected?', 'yes': 'diagnosis_arthritis', 'no': 'diagnosis_general_musculo'}
        ],
        'diagnoses': {
            'diagnosis_fracture': {
                'condition': 'Possible Fracture',
                'confidence': 'High',
                'description': '🦴 **Possible Diagnosis: Fracture**\n\n**URGENT: Go to ER or urgent care immediately**\n\n**Do NOT:**\n- Move the injured area\n- Try to realign bones\n- Apply heat\n\n**Do:**\n- Immobilize the area\n- Apply ice (wrapped in cloth)\n- Elevate if possible\n- Seek immediate medical care',
                'severity': 'high'
            },
            'diagnosis_sprain': {
                'condition': 'Sprain or Strain',
                'confidence': 'High',
                'description': '🤕 **Likely Diagnosis: Sprain/Strain**\n\n**RICE Protocol:**\n1. **R**est - Avoid using injured area\n2. **I**ce - Apply for 15-20 minutes every 2-3 hours\n3. **C**ompression - Use elastic bandage\n4. **E**levation - Raise above heart level\n\n**Recommended Actions:**\n- Take OTC pain relievers\n- See doctor if severe or not improving\n- Gradual return to activity\n\n**Recovery:** 2-6 weeks depending on severity',
                'severity': 'mild'
            },
            'diagnosis_sciatica': {
                'condition': 'Sciatica',
                'confidence': 'Moderate',
                'description': '⚡ **Possible Diagnosis: Sciatica**\n\n**Symptoms:** Back pain radiating down leg\n\n**Recommended Actions:**\n1. Rest but stay active (gentle walking)\n2. Apply heat or ice\n3. Take anti-inflammatory medication\n4. Gentle stretching exercises\n5. See doctor if severe or persistent\n\n**Physical therapy often helps**\n\n**Seek immediate care if:** Loss of bladder/bowel control, severe weakness',
                'severity': 'moderate'
            },
            'diagnosis_back_pain': {
                'condition': 'Lower Back Pain',
                'confidence': 'High',
                'description': '🔙 **Likely Diagnosis: Lower Back Pain**\n\n**Recommended Actions:**\n1. Stay active (bed rest not recommended)\n2. Apply heat or ice\n3. Take OTC pain relievers\n4. Practice good posture\n5. Gentle stretching and strengthening\n\n**Prevention:** Core exercises, proper lifting technique, ergonomic workspace\n\n**See doctor if:** Pain lasts >6 weeks, severe pain, numbness',
                'severity': 'mild'
            },
            'diagnosis_arthritis': {
                'condition': 'Arthritis',
                'confidence': 'Moderate',
                'description': '🦴 **Possible Diagnosis: Arthritis**\n\n**Types:** Osteoarthritis, Rheumatoid arthritis\n\n**Recommended Actions:**\n1. See a rheumatologist for diagnosis\n2. Stay active (low-impact exercise)\n3. Maintain healthy weight\n4. Take anti-inflammatory medication\n5. Apply heat/cold therapy\n\n**Treatment options:** Medication, physical therapy, lifestyle modifications',
                'severity': 'moderate'
            },
            'diagnosis_general_musculo': {
                'condition': 'Musculoskeletal Pain',
                'confidence': 'Low',
                'description': '🏥 **Recommendation: Orthopedic Consultation**\n\nYour symptoms need professional evaluation. Please see an orthopedist or sports medicine doctor.\n\n**Seek immediate care if:** Severe pain, inability to move, signs of infection',
                'severity': 'moderate'
            }
        }
    }
}

def get_comprehensive_diagnosis_category(text):
    """Determine which comprehensive diagnosis tree to use"""
    text_lower = text.lower()
    for category, data in COMPREHENSIVE_DIAGNOSIS_TREES.items():
        for symptom in data['initial_symptoms']:
            if symptom in text_lower:
                return category
    return None
