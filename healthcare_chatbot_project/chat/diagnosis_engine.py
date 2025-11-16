# Interactive Diagnosis Engine - Simplified Version

__all__ = ['DIAGNOSIS_TREES', 'get_diagnosis_category', 'get_first_question', 'get_next_question']

# Diagnosis decision trees
DIAGNOSIS_TREES = {
    'respiratory': {
        'name': 'Respiratory Issues',
        'initial_symptoms': ['cough', 'breathing', 'throat', 'chest', 'congestion', 'sneeze', 'cold', 'flu'],
        'questions': [
            {'id': 'q1', 'question': 'Do you have a fever (temperature above 100.4°F/38°C)?', 'yes': 'q2', 'no': 'q3'},
            {'id': 'q2', 'question': 'Are you experiencing severe body aches and fatigue?', 'yes': 'diagnosis_flu', 'no': 'q4'},
            {'id': 'q3', 'question': 'Do you have a runny or stuffy nose?', 'yes': 'q5', 'no': 'q6'},
            {'id': 'q4', 'question': 'Is your cough producing thick, colored mucus?', 'yes': 'diagnosis_bronchitis', 'no': 'diagnosis_viral_infection'},
            {'id': 'q5', 'question': 'Are you sneezing frequently?', 'yes': 'diagnosis_cold', 'no': 'q7'},
            {'id': 'q6', 'question': 'Do you have difficulty breathing or wheezing?', 'yes': 'diagnosis_asthma', 'no': 'q8'},
            {'id': 'q7', 'question': 'Do you have itchy, watery eyes?', 'yes': 'diagnosis_allergies', 'no': 'diagnosis_cold'},
            {'id': 'q8', 'question': 'Is your cough dry and persistent?', 'yes': 'diagnosis_dry_cough', 'no': 'diagnosis_general_respiratory'}
        ],
        'diagnoses': {
            'diagnosis_flu': {
                'condition': 'Influenza (Flu)',
                'confidence': 'High',
                'description': '🤒 **Likely Diagnosis: Influenza (Flu)**\n\n**Based on your symptoms:** Fever (>100.4°F/38°C), Severe body aches and fatigue, Respiratory symptoms\n\n**Recommended Actions:**\n1. Rest for at least 24 hours after fever subsides\n2. Drink plenty of fluids\n3. Take acetaminophen or ibuprofen for fever and aches\n4. Contact doctor within 48 hours for possible antiviral medication\n\n**When to seek immediate care:** Difficulty breathing, Chest pain or pressure, Sudden dizziness, Severe vomiting\n\n**Recovery time:** 1-2 weeks',
                'severity': 'moderate'
            },
            'diagnosis_cold': {
                'condition': 'Common Cold',
                'confidence': 'High',
                'description': '🤧 **Likely Diagnosis: Common Cold**\n\n**Based on your symptoms:** Runny or stuffy nose, Sneezing, Mild respiratory symptoms, No or low-grade fever\n\n**Recommended Actions:**\n1. Get plenty of rest\n2. Drink warm fluids (tea, soup)\n3. Use saline nasal drops, throat lozenges\n4. Use humidifier\n\n**Duration:** Usually 7-10 days\n\n**When to see a doctor:** Symptoms last more than 10 days, High fever (>101°F/38.3°C), Severe headache or sinus pain, Difficulty breathing',
                'severity': 'mild'
            },
            'diagnosis_bronchitis': {
                'condition': 'Acute Bronchitis',
                'confidence': 'Moderate',
                'description': '😷 **Possible Diagnosis: Acute Bronchitis**\n\n**Based on your symptoms:** Cough with thick, colored mucus, Fever, Chest discomfort\n\n**Recommended Actions:**\n1. See a doctor for proper diagnosis\n2. Rest and allow your body to heal\n3. Drink plenty of fluids to thin mucus\n4. Use humidifier or steam\n5. Avoid irritants (smoke, pollution)\n\n**Duration:** 2-3 weeks\n\n**When to seek immediate care:** Difficulty breathing, Coughing up blood, High fever for more than 3 days',
                'severity': 'moderate'
            },
            'diagnosis_asthma': {
                'condition': 'Asthma Attack',
                'confidence': 'Moderate',
                'description': '🫁 **Possible Diagnosis: Asthma Attack**\n\n**⚠️ IMMEDIATE ACTIONS:**\n1. Use rescue inhaler if you have one\n2. Sit upright - don\'t lie down\n3. Stay calm\n4. Call 911 if: Severe difficulty breathing, Lips turning blue, Rescue inhaler not helping\n\n**If this is your first time:** See a doctor immediately for proper diagnosis and asthma action plan\n\n**This requires medical attention!**',
                'severity': 'high'
            },
            'diagnosis_allergies': {
                'condition': 'Allergic Rhinitis',
                'confidence': 'High',
                'description': '🤧 **Likely Diagnosis: Allergic Rhinitis (Allergies)**\n\n**Based on your symptoms:** Runny or stuffy nose, Itchy watery eyes, Sneezing, No fever\n\n**Recommended Actions:**\n1. Take OTC allergy medication (Claritin, Zyrtec, Allegra)\n2. Avoid triggers (stay indoors during high pollen)\n3. Use saline or corticosteroid nasal spray\n4. Use antihistamine eye drops\n\n**Prevention:** Keep windows closed, use air purifiers, wash bedding weekly',
                'severity': 'mild'
            },
            'diagnosis_dry_cough': {
                'condition': 'Persistent Dry Cough',
                'confidence': 'Moderate',
                'description': '😷 **Possible Diagnosis: Persistent Dry Cough**\n\n**Common Causes:** Post-viral cough, Acid reflux (GERD), Asthma, Allergies, Environmental irritants\n\n**Recommended Actions:**\n1. Drink plenty of water\n2. Take honey (natural cough suppressant)\n3. Use humidifier\n4. Avoid irritants (smoke, dust)\n5. Elevate head while sleeping\n\n**When to see a doctor:** Cough lasting more than 3 weeks, Coughing up blood, Shortness of breath',
                'severity': 'mild'
            },
            'diagnosis_viral_infection': {
                'condition': 'Viral Upper Respiratory Infection',
                'confidence': 'Moderate',
                'description': '🦠 **Likely Diagnosis: Viral Upper Respiratory Infection**\n\n**Recommended Actions:**\n1. Rest and get plenty of sleep\n2. Drink lots of fluids\n3. Use OTC medications for fever and aches\n4. Use humidifier\n\n**Duration:** 7-14 days\n\n**When to see a doctor:** Symptoms worsen after 5 days, High fever persists (>3 days), Difficulty breathing',
                'severity': 'mild'
            },
            'diagnosis_general_respiratory': {
                'condition': 'General Respiratory Symptoms',
                'confidence': 'Low',
                'description': '🏥 **Recommendation: See a Healthcare Provider**\n\nYour symptoms don\'t clearly match a specific condition. Please schedule an appointment with your doctor for proper evaluation.\n\n**Seek immediate care if:** Difficulty breathing, Chest pain, High fever, Coughing up blood',
                'severity': 'unknown'
            }
        }
    },
    'digestive': {
        'name': 'Digestive Issues',
        'initial_symptoms': ['stomach', 'nausea', 'vomit', 'diarrhea', 'abdominal', 'belly', 'digestive'],
        'questions': [
            {'id': 'q1', 'question': 'Do you have a fever?', 'yes': 'q2', 'no': 'q3'},
            {'id': 'q2', 'question': 'Are you experiencing diarrhea?', 'yes': 'diagnosis_gastroenteritis', 'no': 'q4'},
            {'id': 'q3', 'question': 'Is the pain in your upper abdomen?', 'yes': 'q5', 'no': 'q6'},
            {'id': 'q4', 'question': 'Is the pain severe and localized to the lower right abdomen?', 'yes': 'diagnosis_appendicitis', 'no': 'diagnosis_viral_gastro'},
            {'id': 'q5', 'question': 'Does the pain worsen after eating?', 'yes': 'diagnosis_indigestion', 'no': 'q7'},
            {'id': 'q6', 'question': 'Are you constipated?', 'yes': 'diagnosis_constipation', 'no': 'q8'},
            {'id': 'q7', 'question': 'Do you have heartburn or acid reflux?', 'yes': 'diagnosis_gerd', 'no': 'diagnosis_gastritis'},
            {'id': 'q8', 'question': 'Is the pain cramping and comes in waves?', 'yes': 'diagnosis_ibs', 'no': 'diagnosis_general_digestive'}
        ],
        'diagnoses': {
            'diagnosis_gastroenteritis': {
                'condition': 'Gastroenteritis (Stomach Flu)',
                'confidence': 'High',
                'description': '🤢 **Likely Diagnosis: Gastroenteritis**\n\n**Based on your symptoms:** Fever, Diarrhea, Nausea/vomiting, Abdominal pain\n\n**Recommended Actions:**\n1. Hydration is KEY - drink small sips frequently\n2. BRAT diet: Bananas, Rice, Applesauce, Toast\n3. Rest and let your body recover\n4. Anti-diarrheal medication after 24 hours if needed\n\n**Duration:** 1-3 days\n\n**When to seek immediate care:** Severe dehydration, Blood in vomit or stool, High fever (>101°F), Severe abdominal pain',
                'severity': 'moderate'
            },
            'diagnosis_appendicitis': {
                'condition': 'Possible Appendicitis',
                'confidence': 'Moderate',
                'description': '🚨 **URGENT: Possible Appendicitis**\n\n**⚠️ THIS IS A MEDICAL EMERGENCY**\n\n**IMMEDIATE ACTIONS:**\n1. Go to Emergency Room NOW or call 911\n2. Do NOT eat or drink anything\n3. Do NOT take laxatives or use heating pad\n\n**Why it\'s urgent:** Appendix can rupture and cause life-threatening infection. Requires surgery.\n\n**DO NOT DELAY - SEEK EMERGENCY CARE IMMEDIATELY!**',
                'severity': 'emergency'
            },
            'diagnosis_indigestion': {
                'condition': 'Indigestion',
                'confidence': 'High',
                'description': '🍽️ **Likely Diagnosis: Indigestion**\n\n**Recommended Actions:**\n1. Eat smaller, more frequent meals\n2. Avoid fatty, greasy, spicy foods\n3. Don\'t lie down for 2-3 hours after eating\n4. Take OTC antacids (Tums, Rolaids)\n5. Eat slowly and chew thoroughly\n\n**When to see a doctor:** Symptoms persist for more than 2 weeks, Unintended weight loss, Difficulty swallowing',
                'severity': 'mild'
            },
            'diagnosis_constipation': {
                'condition': 'Constipation',
                'confidence': 'High',
                'description': '💩 **Likely Diagnosis: Constipation**\n\n**Recommended Actions:**\n1. Increase fiber (fruits, vegetables, whole grains)\n2. Drink 8-10 glasses of water daily\n3. Exercise - walk 30 minutes daily\n4. Don\'t ignore urge to go\n5. Use OTC laxatives if needed (short-term)\n\n**When to see a doctor:** Constipation lasting more than 3 weeks, Severe pain, Blood in stool',
                'severity': 'mild'
            },
            'diagnosis_gerd': {
                'condition': 'GERD (Acid Reflux)',
                'confidence': 'High',
                'description': '🔥 **Likely Diagnosis: GERD**\n\n**Recommended Actions:**\n1. Elevate head of bed 6-8 inches\n2. Don\'t eat 2-3 hours before bed\n3. Avoid fatty, spicy, acidic foods\n4. Quit smoking, lose weight if overweight\n5. Take antacids or H2 blockers\n\n**When to see a doctor:** Symptoms more than twice a week, OTC medications don\'t help, Difficulty swallowing',
                'severity': 'mild'
            },
            'diagnosis_gastritis': {
                'condition': 'Gastritis',
                'confidence': 'Moderate',
                'description': '🔴 **Possible Diagnosis: Gastritis**\n\n**Recommended Actions:**\n1. Avoid irritants (NSAIDs, alcohol, spicy foods)\n2. Eat smaller, more frequent meals\n3. Take antacids for symptom relief\n4. See a doctor for proper diagnosis\n\n**When to seek immediate care:** Vomiting blood, Black tarry stools, Severe abdominal pain',
                'severity': 'moderate'
            },
            'diagnosis_ibs': {
                'condition': 'Possible IBS',
                'confidence': 'Moderate',
                'description': '🔄 **Possible Diagnosis: IBS (Irritable Bowel Syndrome)**\n\n**Recommended Actions:**\n1. Keep food diary to identify triggers\n2. Try low-FODMAP diet\n3. Increase fiber gradually\n4. Manage stress (yoga, meditation)\n5. See a doctor for proper diagnosis\n\n**IBS is manageable with right approach!**',
                'severity': 'mild'
            },
            'diagnosis_viral_gastro': {
                'condition': 'Viral Gastroenteritis',
                'confidence': 'Moderate',
                'description': '🦠 **Likely Diagnosis: Viral Gastroenteritis**\n\n**Recommended Actions:**\n1. Rest and let your body fight the infection\n2. Hydrate with small sips of clear fluids\n3. Bland diet (BRAT) when ready to eat\n4. Avoid dairy, caffeine, alcohol\n\n**Duration:** 1-3 days\n\n**When to see a doctor:** Symptoms last more than 3 days, Signs of dehydration, High fever',
                'severity': 'mild'
            },
            'diagnosis_general_digestive': {
                'condition': 'General Digestive Discomfort',
                'confidence': 'Low',
                'description': '🏥 **Recommendation: See a Healthcare Provider**\n\nYour symptoms need professional evaluation. Please schedule an appointment with your doctor.\n\n**Seek immediate care if:** Severe abdominal pain, Vomiting blood, Black tarry stools, Signs of dehydration',
                'severity': 'unknown'
            }
        }
    }
}

def get_diagnosis_category(text):
    """Determine which diagnosis tree to use based on symptoms"""
    text_lower = text.lower()
    for category, data in DIAGNOSIS_TREES.items():
        for symptom in data['initial_symptoms']:
            if symptom in text_lower:
                return category
    return None

def get_first_question(category):
    """Get the first question for a diagnosis category"""
    if category not in DIAGNOSIS_TREES:
        return None
    tree = DIAGNOSIS_TREES[category]
    if not tree['questions']:
        return None
    return tree['questions'][0]

def get_next_question(category, current_question_id, answer):
    """Get the next question based on current answer"""
    if category not in DIAGNOSIS_TREES:
        return None
    tree = DIAGNOSIS_TREES[category]
    current_q = None
    for q in tree['questions']:
        if q['id'] == current_question_id:
            current_q = q
            break
    if not current_q:
        return None
    next_id = current_q.get('yes' if answer else 'no')
    if next_id and next_id.startswith('diagnosis_'):
        diagnosis_key = next_id
        if diagnosis_key in tree['diagnoses']:
            return {'type': 'diagnosis', 'data': tree['diagnoses'][diagnosis_key]}
    for q in tree['questions']:
        if q['id'] == next_id:
            return {'type': 'question', 'data': q}
    return None
