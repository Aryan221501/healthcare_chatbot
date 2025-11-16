# Medical Knowledge Base - Comprehensive Disease Information

MEDICAL_KB = {
    'en': {
        # Common Cold & Flu
        'cold': {
            'symptoms': ['cold', 'runny nose', 'sneezing', 'stuffy nose', 'congestion'],
            'response': """🤧 **Common Cold**

**Symptoms:**
• Runny or stuffy nose
• Sneezing
• Sore throat
• Mild cough
• Mild body aches
• Low-grade fever (rare)

**Treatment:**
• Rest and stay hydrated
• Drink warm fluids (tea, soup)
• Use saline nasal drops
• Take over-the-counter pain relievers
• Use a humidifier

**Duration:** Usually 7-10 days

**When to see a doctor:**
• Symptoms last more than 10 days
• High fever (>101°F/38.3°C)
• Severe headache or sinus pain
• Difficulty breathing

**Prevention:**
• Wash hands frequently
• Avoid close contact with sick people
• Don't touch your face"""
        },
        
        'flu': {
            'symptoms': ['flu', 'influenza', 'body ache', 'chills', 'fatigue'],
            'response': """🤒 **Influenza (Flu)**

**Symptoms:**
• High fever (100-104°F/38-40°C)
• Severe body aches
• Extreme fatigue
• Dry cough
• Headache
• Chills and sweats
• Sore throat

**Treatment:**
• Rest for at least 24 hours after fever subsides
• Drink plenty of fluids
• Antiviral medications (if prescribed within 48 hours)
• Pain relievers for aches and fever
• Stay home to avoid spreading

**Duration:** 1-2 weeks

**When to see a doctor:**
• Difficulty breathing or shortness of breath
• Chest pain or pressure
• Sudden dizziness or confusion
• Severe vomiting
• Symptoms improve but return with fever

**High-risk groups:**
• Young children, elderly, pregnant women
• People with chronic conditions

**Prevention:**
• Annual flu vaccine
• Good hand hygiene
• Avoid crowded places during flu season"""
        },

        # Fever
        'fever': {
            'symptoms': ['fever', 'temperature', 'high temperature', 'feverish', 'hot'],
            'response': """🌡️ **Fever**

**Temperature Ranges:**
• Normal: 97-99°F (36.1-37.2°C)
• Low-grade: 99-100.4°F (37.2-38°C)
• Moderate: 100.4-102.2°F (38-39°C)
• High: 102.2-104°F (39-40°C)
• Very high: >104°F (>40°C)

**Common Causes:**
• Viral infections (cold, flu)
• Bacterial infections
• Heat exhaustion
• Inflammatory conditions
• Medications

**Treatment:**
• Rest and stay hydrated
• Take acetaminophen or ibuprofen
• Wear light clothing
• Use lukewarm sponge bath
• Keep room temperature comfortable

**When to seek immediate care:**
• Fever >103°F (39.4°C) in adults
• Fever >100.4°F (38°C) in infants <3 months
• Fever lasting >3 days
• Severe headache or stiff neck
• Difficulty breathing
• Chest pain
• Confusion or seizures
• Severe abdominal pain

**For Children:**
• Fever with rash
• Persistent crying
• Difficulty waking up
• Not drinking fluids"""
        },

        # Cough
        'cough': {
            'symptoms': ['cough', 'coughing', 'persistent cough', 'dry cough', 'wet cough'],
            'response': """😷 **Cough**

**Types:**
• **Dry cough:** No mucus, tickling sensation
• **Wet cough:** Produces mucus/phlegm
• **Chronic cough:** Lasts >8 weeks

**Common Causes:**
• Viral infections (cold, flu)
• Allergies
• Asthma
• Acid reflux (GERD)
• Postnasal drip
• Smoking

**Treatment:**
• Stay hydrated (thins mucus)
• Use honey (for adults and children >1 year)
• Throat lozenges
• Humidifier or steam inhalation
• Avoid irritants (smoke, dust)
• Elevate head while sleeping

**When to see a doctor:**
• Cough lasting >3 weeks
• Coughing up blood
• Difficulty breathing or wheezing
• High fever
• Chest pain
• Thick, green/yellow mucus
• Night sweats or weight loss

**Red Flags:**
• Sudden severe cough with choking
• Cough after inhaling foreign object
• Severe shortness of breath"""
        },

        # Headache
        'headache': {
            'symptoms': ['headache', 'head pain', 'migraine', 'head hurts'],
            'response': """🤕 **Headache**

**Types:**
• **Tension headache:** Tight band around head
• **Migraine:** Throbbing, one-sided, with nausea
• **Cluster headache:** Severe, around one eye
• **Sinus headache:** Pressure in face/forehead

**Common Triggers:**
• Stress and tension
• Dehydration
• Lack of sleep
• Eye strain
• Caffeine withdrawal
• Certain foods
• Hormonal changes

**Treatment:**
• Rest in quiet, dark room
• Apply cold or warm compress
• Stay hydrated
• Over-the-counter pain relievers
• Gentle neck/shoulder massage
• Relaxation techniques

**When to seek immediate care:**
• Sudden, severe "thunderclap" headache
• Headache with fever and stiff neck
• Headache after head injury
• Confusion or difficulty speaking
• Vision changes or weakness
• Worst headache of your life
• Headache with seizures

**Prevention:**
• Regular sleep schedule
• Stay hydrated
• Manage stress
• Limit caffeine
• Regular exercise"""
        },

        # Stomach Issues
        'stomach': {
            'symptoms': ['stomach ache', 'stomach pain', 'abdominal pain', 'belly pain', 'nausea', 'vomiting', 'diarrhea'],
            'response': """🤢 **Stomach/Abdominal Issues**

**Common Causes:**
• Food poisoning
• Gastroenteritis (stomach flu)
• Indigestion
• Constipation
• Gas and bloating
• Acid reflux
• Stress

**Treatment:**
• Rest your stomach (clear liquids first)
• BRAT diet (Bananas, Rice, Applesauce, Toast)
• Stay hydrated (small sips frequently)
• Avoid dairy, fatty, spicy foods
• Ginger tea for nausea
• Peppermint for gas/bloating

**When to see a doctor:**
• Severe abdominal pain
• Blood in vomit or stool
• High fever (>101°F/38.3°C)
• Signs of dehydration (dark urine, dizziness)
• Persistent vomiting (>24 hours)
• Abdominal pain with pregnancy
• Recent abdominal injury

**Emergency Signs:**
• Sudden, severe pain
• Rigid, board-like abdomen
• Pain with fever and vomiting
• Inability to pass stool or gas
• Chest pain radiating to abdomen

**Prevention:**
• Wash hands before eating
• Cook food thoroughly
• Avoid contaminated water
• Eat slowly and chew well"""
        },

        # Allergies
        'allergy': {
            'symptoms': ['allergy', 'allergies', 'allergic', 'itchy', 'rash', 'hives', 'sneezing'],
            'response': """🤧 **Allergies**

**Common Types:**
• Seasonal (pollen, grass, trees)
• Food allergies
• Pet dander
• Dust mites
• Mold
• Insect stings

**Symptoms:**
• Sneezing and runny nose
• Itchy, watery eyes
• Skin rash or hives
• Swelling
• Difficulty breathing (severe)

**Treatment:**
• Antihistamines (Benadryl, Claritin, Zyrtec)
• Nasal corticosteroid sprays
• Decongestants
• Eye drops
• Avoid known allergens

**When to seek immediate care:**
• Difficulty breathing or swallowing
• Swelling of face, lips, or tongue
• Rapid pulse
• Dizziness or fainting
• Severe hives or rash spreading rapidly

**Anaphylaxis (Life-threatening):**
• Use EpiPen if available
• Call 911 immediately
• Lie down with legs elevated
• Don't stand up suddenly

**Prevention:**
• Identify and avoid triggers
• Keep windows closed during high pollen
• Use air purifiers
• Wash bedding in hot water weekly
• Read food labels carefully"""
        },

        # Diabetes
        'diabetes': {
            'symptoms': ['diabetes', 'blood sugar', 'high sugar', 'diabetic', 'insulin'],
            'response': """🩸 **Diabetes**

**Types:**
• **Type 1:** Body doesn't produce insulin
• **Type 2:** Body doesn't use insulin properly
• **Gestational:** During pregnancy

**Symptoms:**
• Increased thirst and urination
• Extreme hunger
• Unexplained weight loss
• Fatigue
• Blurred vision
• Slow-healing sores
• Frequent infections

**Management:**
• Monitor blood sugar regularly
• Take medications as prescribed
• Healthy diet (low sugar, complex carbs)
• Regular exercise
• Maintain healthy weight
• Regular check-ups

**Complications (if uncontrolled):**
• Heart disease
• Kidney damage
• Eye damage
• Nerve damage
• Foot problems

**Emergency Signs:**
• Very high blood sugar (>300 mg/dL)
• Very low blood sugar (<70 mg/dL)
• Confusion or unconsciousness
• Rapid breathing
• Fruity breath odor

**Prevention (Type 2):**
• Maintain healthy weight
• Exercise regularly
• Eat balanced diet
• Limit processed foods and sugar
• Regular health screenings"""
        },

        # Hypertension
        'hypertension': {
            'symptoms': ['high blood pressure', 'hypertension', 'blood pressure', 'bp'],
            'response': """💓 **High Blood Pressure (Hypertension)**

**Blood Pressure Ranges:**
• Normal: <120/80 mmHg
• Elevated: 120-129/<80 mmHg
• Stage 1: 130-139/80-89 mmHg
• Stage 2: ≥140/90 mmHg
• Crisis: >180/120 mmHg

**Often Called "Silent Killer":**
• Usually no symptoms
• Can cause serious damage over time

**Risk Factors:**
• Age (increases with age)
• Family history
• Obesity
• Lack of exercise
• High salt diet
• Smoking
• Excessive alcohol
• Stress
• Chronic conditions

**Management:**
• Take medications as prescribed
• Reduce sodium intake (<2,300 mg/day)
• DASH diet (fruits, vegetables, whole grains)
• Regular exercise (30 min/day)
• Maintain healthy weight
• Limit alcohol
• Quit smoking
• Manage stress
• Regular monitoring

**Complications:**
• Heart attack
• Stroke
• Heart failure
• Kidney disease
• Vision loss

**Emergency (Hypertensive Crisis):**
• Severe headache
• Chest pain
• Difficulty breathing
• Severe anxiety
• Nosebleeds
→ Call 911 immediately"""
        },

        # Asthma
        'asthma': {
            'symptoms': ['asthma', 'wheezing', 'shortness of breath', 'breathing difficulty', 'breathless'],
            'response': """🫁 **Asthma**

**Symptoms:**
• Wheezing (whistling sound when breathing)
• Shortness of breath
• Chest tightness
• Coughing (especially at night)
• Difficulty breathing

**Common Triggers:**
• Allergens (pollen, dust, pet dander)
• Cold air
• Exercise
• Smoke
• Strong odors
• Respiratory infections
• Stress

**Management:**
• Use prescribed inhalers correctly
• Avoid known triggers
• Take controller medications daily
• Keep rescue inhaler accessible
• Monitor peak flow
• Get flu vaccine annually

**Asthma Action Plan:**
• **Green Zone:** Doing well, no symptoms
• **Yellow Zone:** Caution, symptoms present
• **Red Zone:** Medical alert, severe symptoms

**When to seek immediate care:**
• Severe difficulty breathing
• Lips or fingernails turning blue
• Rapid pulse
• Sweating
• Anxiety or panic
• Rescue inhaler not helping
• Can't speak in full sentences

**Emergency Treatment:**
• Use rescue inhaler
• Sit upright
• Stay calm
• Call 911 if not improving

**Prevention:**
• Identify and avoid triggers
• Take medications as prescribed
• Regular check-ups
• Keep home clean and dust-free"""
        },

        # Heart Disease
        'heart': {
            'symptoms': ['heart', 'chest pain', 'heart attack', 'cardiac', 'angina'],
            'response': """❤️ **Heart Disease & Chest Pain**

**⚠️ HEART ATTACK WARNING SIGNS:**
• Chest pain/pressure (may radiate to arm, jaw, back)
• Shortness of breath
• Cold sweats
• Nausea or vomiting
• Lightheadedness
• Extreme fatigue

**🚨 IF YOU SUSPECT HEART ATTACK:**
1. Call 911 IMMEDIATELY
2. Chew aspirin (if not allergic)
3. Sit down and stay calm
4. Don't drive yourself

**Types of Heart Disease:**
• Coronary artery disease
• Heart failure
• Arrhythmias
• Heart valve disease

**Risk Factors:**
• High blood pressure
• High cholesterol
• Diabetes
• Smoking
• Obesity
• Lack of exercise
• Family history
• Age
• Stress

**Prevention:**
• Eat heart-healthy diet
• Exercise regularly (150 min/week)
• Maintain healthy weight
• Don't smoke
• Limit alcohol
• Manage stress
• Control blood pressure and cholesterol
• Regular check-ups

**Symptoms to Monitor:**
• Chest discomfort
• Shortness of breath
• Irregular heartbeat
• Swelling in legs/feet
• Persistent fatigue

**When to see a doctor:**
• Any chest pain or discomfort
• Shortness of breath with activity
• Irregular heartbeat
• Swelling in extremities
• Unexplained fatigue"""
        },

        # Mental Health
        'mental_health': {
            'symptoms': ['depression', 'anxiety', 'stress', 'mental health', 'sad', 'worried', 'panic'],
            'response': """🧠 **Mental Health**

**Common Conditions:**

**Depression:**
• Persistent sadness
• Loss of interest in activities
• Changes in sleep/appetite
• Fatigue
• Difficulty concentrating
• Feelings of worthlessness

**Anxiety:**
• Excessive worry
• Restlessness
• Rapid heartbeat
• Difficulty concentrating
• Sleep problems
• Panic attacks

**Stress:**
• Feeling overwhelmed
• Irritability
• Headaches
• Muscle tension
• Difficulty sleeping

**Self-Care Strategies:**
• Regular exercise
• Adequate sleep (7-9 hours)
• Healthy diet
• Mindfulness/meditation
• Social connections
• Limit alcohol and caffeine
• Set realistic goals
• Take breaks

**When to seek help:**
• Symptoms interfere with daily life
• Thoughts of self-harm
• Substance abuse
• Symptoms lasting >2 weeks
• Unable to cope with daily tasks

**Crisis Resources:**
• **National Suicide Prevention Lifeline:** 988
• **Crisis Text Line:** Text HOME to 741741
• **Emergency:** Call 911

**Treatment Options:**
• Therapy (CBT, counseling)
• Medications (if prescribed)
• Support groups
• Lifestyle changes

**Remember:**
• Mental health is as important as physical health
• Seeking help is a sign of strength
• Recovery is possible
• You're not alone"""
        },

        # COVID-19
        'covid': {
            'symptoms': ['covid', 'coronavirus', 'covid-19', 'corona'],
            'response': """🦠 **COVID-19**

**Common Symptoms:**
• Fever or chills
• Cough
• Shortness of breath
• Fatigue
• Body aches
• Loss of taste or smell
• Sore throat
• Congestion
• Nausea or vomiting
• Diarrhea

**When to Get Tested:**
• You have symptoms
• Exposed to someone with COVID-19
• Before gathering with high-risk individuals

**Treatment (Mild Cases):**
• Rest and stay hydrated
• Over-the-counter medications for symptoms
• Isolate from others
• Monitor symptoms

**When to seek immediate care:**
• Difficulty breathing
• Persistent chest pain
• Confusion
• Inability to wake or stay awake
• Bluish lips or face

**Prevention:**
• Get vaccinated and boosted
• Wear masks in crowded indoor spaces
• Practice good hand hygiene
• Maintain physical distance when sick
• Improve ventilation
• Stay home when sick

**Isolation Guidelines:**
• Stay home for at least 5 days
• Wear mask around others
• Test before ending isolation

**Long COVID:**
• Symptoms lasting >4 weeks
• Fatigue, brain fog, shortness of breath
• Consult doctor if experiencing"""
        },

        # General Health
        'general': {
            'symptoms': ['health', 'healthy', 'wellness', 'checkup', 'prevention'],
            'response': """🏥 **General Health & Wellness**

**Preventive Care:**
• Annual physical exam
• Dental checkups (every 6 months)
• Eye exams
• Age-appropriate screenings
• Vaccinations up to date

**Healthy Lifestyle:**
• **Exercise:** 150 min moderate activity/week
• **Diet:** Fruits, vegetables, whole grains, lean protein
• **Sleep:** 7-9 hours per night
• **Hydration:** 8 glasses of water daily
• **Stress management:** Meditation, hobbies, relaxation

**Important Screenings:**
• Blood pressure
• Cholesterol
• Blood sugar
• Cancer screenings (age-appropriate)
• Bone density (for women >65)

**Warning Signs to Never Ignore:**
• Chest pain
• Sudden severe headache
• Difficulty breathing
• Sudden weakness or numbness
• Severe abdominal pain
• Coughing up blood
• Suicidal thoughts

**When to See a Doctor:**
• Annual checkup
• New or worsening symptoms
• Chronic condition management
• Medication refills
• Health concerns

**Emergency (Call 911):**
• Chest pain
• Difficulty breathing
• Severe bleeding
• Loss of consciousness
• Stroke symptoms (FAST)
• Severe allergic reaction"""
        }
    },
    
    'hi': {
        # Hindi translations for key conditions
        'fever': {
            'symptoms': ['बुखार', 'तापमान', 'गर्मी'],
            'response': """🌡️ **बुखार**

**तापमान सीमा:**
• सामान्य: 97-99°F (36.1-37.2°C)
• हल्का: 99-100.4°F (37.2-38°C)
• मध्यम: 100.4-102.2°F (38-39°C)
• उच्च: 102.2-104°F (39-40°C)

**उपचार:**
• आराम करें और हाइड्रेटेड रहें
• पैरासिटामोल या इबुप्रोफेन लें
• हल्के कपड़े पहनें
• गुनगुने पानी से स्पंज बाथ

**डॉक्टर से कब मिलें:**
• बुखार >103°F (39.4°C)
• 3 दिन से अधिक समय तक बुखार
• गंभीर सिरदर्द
• सांस लेने में कठिनाई
• सीने में दर्द"""
        },
        
        'cough': {
            'symptoms': ['खांसी', 'खाँसी', 'कफ'],
            'response': """😷 **खांसी**

**प्रकार:**
• सूखी खांसी: बिना बलगम
• गीली खांसी: बलगम के साथ

**उपचार:**
• पानी पिएं (बलगम को पतला करता है)
• शहद का उपयोग करें
• भाप लें
• धूम्रपान से बचें

**डॉक्टर से कब मिलें:**
• 3 सप्ताह से अधिक खांसी
• खून के साथ खांसी
• सांस लेने में कठिनाई
• तेज बुखार
• सीने में दर्द"""
        }
    }
}

# Emergency keywords that trigger immediate medical attention
EMERGENCY_KEYWORDS = {
    'en': [
        'chest pain', 'heart attack', 'can\'t breathe', 'difficulty breathing',
        'severe bleeding', 'unconscious', 'suicide', 'overdose',
        'stroke', 'seizure', 'severe pain', 'choking'
    ],
    'hi': [
        'सीने में दर्द', 'दिल का दौरा', 'सांस नहीं ले सकता',
        'गंभीर रक्तस्राव', 'बेहोश', 'आत्महत्या'
    ]
}

EMERGENCY_RESPONSE = {
    'en': """🚨 **MEDICAL EMERGENCY**

Based on your symptoms, this could be a medical emergency!

**CALL 911 IMMEDIATELY or go to the nearest emergency room**

**While waiting for help:**
• Stay calm
• Don't move if injured
• If chest pain: Sit down, chew aspirin (if not allergic)
• If choking: Perform Heimlich maneuver
• If bleeding: Apply pressure with clean cloth

**Emergency Numbers:**
• Emergency: 911
• Poison Control: 1-800-222-1222
• Suicide Prevention: 988

This chatbot is NOT a substitute for emergency medical care.
Please seek immediate professional help!""",
    
    'hi': """🚨 **चिकित्सा आपातकाल**

आपके लक्षणों के आधार पर, यह एक चिकित्सा आपातकाल हो सकता है!

**तुरंत 102/108 पर कॉल करें या निकटतम अस्पताल जाएं**

**मदद का इंतजार करते समय:**
• शांत रहें
• चोट लगने पर न हिलें
• सीने में दर्द: बैठ जाएं, एस्पिरिन लें
• रक्तस्राव: साफ कपड़े से दबाव डालें

यह चैटबॉट आपातकालीन चिकित्सा देखभाल का विकल्प नहीं है।
कृपया तुरंत पेशेवर मदद लें!"""
}
