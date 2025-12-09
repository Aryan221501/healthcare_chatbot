from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Conversation
from .medical_kb import MEDICAL_KB, EMERGENCY_KEYWORDS, EMERGENCY_RESPONSE
from .gemini_integration import get_gemini_response, get_gemini_diagnosis, is_gemini_available
from .diagnosis_engine import get_diagnosis_category, get_first_question, get_next_question, DIAGNOSIS_TREES
from .comprehensive_diagnosis import COMPREHENSIVE_DIAGNOSIS_TREES, get_comprehensive_diagnosis_category
import re, uuid

# Store diagnosis sessions and conversation history
diagnosis_sessions = {}
conversation_histories = {}

def detect_language(text):
    """Detect if text is in Hindi or English"""
    if re.search(r'[\u0900-\u097F]', text):
        return 'hi'
    return 'en'

def match_medical_condition(lang, text):
    """Match user input to medical conditions in knowledge base"""
    text_lower = text.lower()
    kb = MEDICAL_KB.get(lang, MEDICAL_KB['en'])
    
    # Check for emergency keywords first
    emergency_keywords = EMERGENCY_KEYWORDS.get(lang, EMERGENCY_KEYWORDS['en'])
    for keyword in emergency_keywords:
        if keyword.lower() in text_lower:
            return EMERGENCY_RESPONSE.get(lang, EMERGENCY_RESPONSE['en'])
    
    # Check each medical condition
    for condition_name, condition_data in kb.items():
        symptoms = condition_data.get('symptoms', [])
        for symptom in symptoms:
            if symptom.lower() in text_lower:
                return condition_data['response']
    
    return None

def match_kb(lang, text):
    """Main knowledge base matching function"""
    text_lower = text.lower()
    
    # Greetings
    greetings_en = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']
    greetings_hi = ['नमस्ते', 'हैलो', 'हाय', 'नमस्कार']
    
    if lang == 'en':
        for greeting in greetings_en:
            if greeting in text_lower:
                return """<h3>Hello! I'm your Healthcare Assistant</h3>

<p>I can help you with information about:</p>
<ul>
<li>Common illnesses (cold, flu, fever, cough)</li>
<li>Chronic conditions (diabetes, hypertension, asthma)</li>
<li>Symptoms and treatments</li>
<li>When to see a doctor</li>
<li>Emergency situations</li>
<li>General health and wellness</li>
</ul>

<h4>How to use</h4>
<ul>
<li>Describe your symptoms (e.g., "I have a fever and cough")</li>
<li>Ask about a condition (e.g., "Tell me about diabetes")</li>
<li>Type "help" for more information</li>
</ul>

<p><em>Important: This is for informational purposes only. Always consult a healthcare professional for medical advice.</em></p>

<p>What can I help you with today?</p>"""
    else:
        for greeting in greetings_hi:
            if greeting in text_lower:
                return """<h3>नमस्ते! मैं आपका स्वास्थ्य सहायक हूं</h3>

<p>मैं आपकी मदद कर सकता हूं:</p>
<ul>
<li>सामान्य बीमारियां (सर्दी, फ्लू, बुखार, खांसी)</li>
<li>पुरानी स्थितियां (मधुमेह, उच्च रक्तचाप, अस्थमा)</li>
<li>लक्षण और उपचार</li>
<li>डॉक्टर से कब मिलें</li>
<li>आपातकालीन स्थितियां</li>
</ul>

<p>अपने लक्षण बताएं या किसी स्थिति के बारे में पूछें।</p>"""
    
    # Help command
    if 'help' in text_lower or 'सहाय' in text_lower:
        if lang == 'en':
            return """<h3>How I Can Help</h3>

<h4>Available Topics</h4>
<ul>
<li><strong>Common Illnesses:</strong> Cold, flu, fever, cough, headache</li>
<li><strong>Digestive Issues:</strong> Stomach pain, nausea, diarrhea</li>
<li><strong>Chronic Conditions:</strong> Diabetes, hypertension, asthma, heart disease</li>
<li><strong>Allergies:</strong> Seasonal, food, skin reactions</li>
<li><strong>Mental Health:</strong> Depression, anxiety, stress</li>
<li><strong>COVID-19:</strong> Symptoms, prevention, treatment</li>
<li><strong>General Health:</strong> Wellness tips, preventive care</li>
</ul>

<h4>Example Questions</h4>
<ul>
<li>"I have a fever and body aches"</li>
<li>"What are the symptoms of diabetes?"</li>
<li>"How do I manage high blood pressure?"</li>
<li>"I'm feeling anxious and stressed"</li>
</ul>

<p><strong style="color: #ef4444;">Emergency:</strong> If you're experiencing a medical emergency, call 911 immediately!</p>

<p>What would you like to know about?</p>"""
        else:
            return """<h3>मैं कैसे मदद कर सकता हूं</h3>

<h4>उपलब्ध विषय</h4>
<ul>
<li>सामान्य बीमारियां</li>
<li>पाचन समस्याएं</li>
<li>पुरानी स्थितियां</li>
<li>एलर्जी</li>
<li>मानसिक स्वास्थ्य</li>
</ul>

<p>अपने लक्षण या प्रश्न बताएं।</p>"""
    
    # Try to match medical condition
    medical_response = match_medical_condition(lang, text)
    if medical_response:
        return medical_response
    
    # Fallback response
    if lang == 'en':
        return """<p>I'm not sure I understand your question.</p>

<h4>Try</h4>
<ul>
<li>Describing your symptoms (e.g., "I have a headache")</li>
<li>Asking about a specific condition (e.g., "What is diabetes?")</li>
<li>Typing "help" to see what I can assist with</li>
</ul>

<h4>Common topics I can help with</h4>
<ul>
<li>Fever, cough, cold, flu</li>
<li>Headaches and body aches</li>
<li>Stomach problems</li>
<li>Allergies</li>
<li>Chronic conditions (diabetes, hypertension, asthma)</li>
<li>Mental health</li>
<li>General wellness</li>
</ul>

<p>What would you like to know?</p>"""
    else:
        return """<p>मुझे आपका प्रश्न समझ नहीं आया।</p>

<p>कृपया अपने लक्षण बताएं या "help" टाइप करें।</p>"""

@ensure_csrf_cookie
def index(request):
    return render(request, 'chat/index.html', {})

def message_api(request):
    if request.method=='POST':
        try:
            text = request.POST.get('text','').strip()
            if not text:
                return JsonResponse({'error': 'No text provided'}, status=400)
            
            session = request.POST.get('session','')
            if not session:
                session = str(uuid.uuid4())
            
            lang = detect_language(text)
            response = None
            powered_by = 'rules'
            
            # Check if user is in diagnosis mode
            if session in diagnosis_sessions:
                response = handle_diagnosis_response(session, text, lang)
                powered_by = 'diagnosis_engine'
            
            # Check if user wants to start diagnosis (traditional decision tree)
            elif 'diagnose' in text.lower() and ('start' in text.lower() or 'begin' in text.lower()):
                response = start_diagnosis(session, text, lang)
                powered_by = 'diagnosis_engine'
            
            # Check if user is asking for diagnosis using AI
            elif any(keyword in text.lower() for keyword in ['diagnose', 'diagnosis', 'what do i have', 'what is wrong', 'run a diagnosis']):
                if is_gemini_available():
                    # Get conversation history for context
                    history = conversation_histories.get(session, [])
                    
                    # Use Gemini AI for intelligent diagnosis
                    ai_diagnosis = get_gemini_diagnosis(text, history)
                    
                    if ai_diagnosis:
                        response = ai_diagnosis
                        powered_by = 'gemini_diagnosis'
                        
                        # Update conversation history
                        history.append({"role": "user", "content": text})
                        history.append({"role": "assistant", "content": response})
                        conversation_histories[session] = history[-10:]
                        
                        print(f"✅ Gemini AI diagnosis completed")
                    else:
                        # Fallback to traditional diagnosis
                        response = start_diagnosis(session, text, lang)
                        powered_by = 'diagnosis_engine'
                else:
                    # Use traditional diagnosis if AI not available
                    response = start_diagnosis(session, text, lang)
                    powered_by = 'diagnosis_engine'
            
            # Try Google Gemini AI for all other queries (FREE!)
            elif is_gemini_available():
                # Get conversation history for this session
                history = conversation_histories.get(session, [])
                
                # Get AI response
                ai_response = get_gemini_response(text, history)
                
                if ai_response:
                    response = ai_response
                    powered_by = 'gemini_ai'
                    
                    # Update conversation history
                    history.append({"role": "user", "content": text})
                    history.append({"role": "assistant", "content": response})
                    # Keep only last 10 messages (5 exchanges)
                    conversation_histories[session] = history[-10:]
                    
                    print(f"✅ Gemini AI responded successfully")
                else:
                    print(f"⚠️ Gemini AI returned None, using fallback")
                    # Fallback to rule-based if AI fails
                    response = match_kb(lang, text)
                    powered_by = 'rules'
            
            # Use rule-based system if AI not available
            if not response:
                print(f"ℹ️ Using rule-based system")
                response = match_kb(lang, text)
                powered_by = 'rules'
            
            # Try to save to database
            try:
                Conversation.objects.create(session_id=session, user_text=text, bot_text=response, language=lang)
            except Exception as db_error:
                print(f"Database error (non-critical): {db_error}")
            
            return JsonResponse({
                'session': session,
                'response': response,
                'language': lang,
                'powered_by': powered_by
            })
        except Exception as e:
            print(f"❌ Error in message_api: {e}")
            import traceback
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error':'POST required'}, status=400)

def start_diagnosis(session, text, lang):
    """Start an interactive diagnosis session"""
    if lang != 'en':
        return "Diagnosis feature is currently available in English only. / निदान सुविधा वर्तमान में केवल अंग्रेजी में उपलब्ध है।"
    
    # Try comprehensive diagnosis first
    category = get_comprehensive_diagnosis_category(text)
    diagnosis_tree = COMPREHENSIVE_DIAGNOSIS_TREES
    
    # Fall back to original diagnosis if not found
    if not category:
        category = get_diagnosis_category(text)
        diagnosis_tree = DIAGNOSIS_TREES
    
    if not category:
        return """🔍 **Interactive Diagnosis System**

I can help diagnose your condition by asking you a series of yes/no questions.

**Available diagnosis categories:**

**🫁 Respiratory Issues:**
• Cough, cold, flu, breathing problems, asthma, bronchitis

**🤢 Digestive Issues:**
• Stomach pain, nausea, diarrhea, constipation, GERD

**❤️ Cardiovascular Issues:**
• Chest pain, heart palpitations, irregular heartbeat

**🧠 Neurological Issues:**
• Headache, migraine, dizziness, numbness, tingling

**🌿 Skin Issues:**
• Rash, itching, acne, eczema, psoriasis

**💙 Mental Health:**
• Anxiety, depression, stress, panic attacks

**🦴 Muscle & Joint Issues:**
• Back pain, joint pain, arthritis, sprains

**To start, describe your main symptoms. For example:**
• "I have chest pain"
• "I have a severe headache"
• "I have a rash on my arm"
• "I'm feeling anxious"

Or type "diagnose [category]" to start."""
    
    # Get first question from appropriate tree
    if category in COMPREHENSIVE_DIAGNOSIS_TREES:
        tree = COMPREHENSIVE_DIAGNOSIS_TREES[category]
        first_question = tree['questions'][0] if tree['questions'] else None
    else:
        first_question = get_first_question(category)
    
    if not first_question:
        return "Sorry, I couldn't start the diagnosis. Please try describing your symptoms."
    
    # Store diagnosis session
    diagnosis_sessions[session] = {
        'category': category,
        'current_question': first_question['id'],
        'answers': [],
        'tree_type': 'comprehensive' if category in COMPREHENSIVE_DIAGNOSIS_TREES else 'original'
    }
    
    return f"""🔍 **Starting Interactive Diagnosis: {diagnosis_tree[category]['name']}**

I'll ask you a series of yes/no questions to help identify your condition.

**Please answer with "yes" or "no"**

**Question 1:**
{first_question['question']}

Type "yes" or "no" to continue.
Type "cancel" to stop the diagnosis."""

def handle_diagnosis_response(session, text, lang):
    """Handle user's answer in diagnosis session"""
    text_lower = text.lower().strip()
    
    # Check if user wants to cancel
    if text_lower in ['cancel', 'stop', 'quit', 'exit']:
        del diagnosis_sessions[session]
        return "Diagnosis cancelled. How else can I help you?"
    
    # Parse yes/no answer
    if text_lower in ['yes', 'y', 'yeah', 'yep', 'yup']:
        answer = True
    elif text_lower in ['no', 'n', 'nope', 'nah']:
        answer = False
    else:
        return """Please answer with **"yes"** or **"no"**.

Type "cancel" if you want to stop the diagnosis."""
    
    # Get current session data
    session_data = diagnosis_sessions[session]
    category = session_data['category']
    current_question_id = session_data['current_question']
    tree_type = session_data.get('tree_type', 'original')
    
    # Store answer
    session_data['answers'].append({
        'question_id': current_question_id,
        'answer': answer
    })
    
    # Get next question or diagnosis based on tree type
    if tree_type == 'comprehensive':
        # Use comprehensive diagnosis tree
        tree = COMPREHENSIVE_DIAGNOSIS_TREES[category]
        current_q = None
        for q in tree['questions']:
            if q['id'] == current_question_id:
                current_q = q
                break
        
        if not current_q:
            del diagnosis_sessions[session]
            return "Sorry, something went wrong. Please try again."
        
        next_id = current_q.get('yes' if answer else 'no')
        
        if next_id and next_id.startswith('diagnosis_'):
            # We have a diagnosis
            diagnosis = tree['diagnoses'].get(next_id)
            if diagnosis:
                del diagnosis_sessions[session]
                next_step = {'type': 'diagnosis', 'data': diagnosis}
            else:
                del diagnosis_sessions[session]
                return "Sorry, something went wrong. Please try again."
        else:
            # Get next question
            next_q = None
            for q in tree['questions']:
                if q['id'] == next_id:
                    next_q = q
                    break
            if next_q:
                next_step = {'type': 'question', 'data': next_q}
            else:
                del diagnosis_sessions[session]
                return "Sorry, something went wrong. Please try again."
    else:
        # Use original diagnosis tree
        next_step = get_next_question(category, current_question_id, answer)
    
    if not next_step:
        del diagnosis_sessions[session]
        return "Sorry, something went wrong with the diagnosis. Please try again."
    
    if next_step['type'] == 'diagnosis':
        # We have a diagnosis!
        diagnosis = next_step['data']
        del diagnosis_sessions[session]
        
        # Format final diagnosis
        severity_emoji = {
            'emergency': '🚨',
            'high': '⚠️',
            'moderate': '🔶',
            'mild': '✅',
            'unknown': '❓'
        }
        
        emoji = severity_emoji.get(diagnosis.get('severity', 'unknown'), '🏥')
        
        return f"""{emoji} **Diagnosis Complete**

{diagnosis['description']}

**Confidence Level:** {diagnosis.get('confidence', 'Moderate')}

---

**Disclaimer:** This is an automated assessment based on your answers. It is NOT a substitute for professional medical advice. Please consult a healthcare provider for proper diagnosis and treatment.

Would you like to:
• Start a new diagnosis (type "diagnose")
• Ask about a specific condition
• Get general health information (type "help")"""
    
    else:
        # Ask next question
        next_question = next_step['data']
        session_data['current_question'] = next_question['id']
        
        # Count questions
        question_num = len(session_data['answers']) + 1
        
        return f"""**Question {question_num}:**
{next_question['question']}

Type "yes" or "no" to continue.
Type "cancel" to stop the diagnosis."""
