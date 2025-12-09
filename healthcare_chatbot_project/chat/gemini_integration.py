"""
Google Gemini Integration - 100% FREE!
Provides intelligent responses using Google's Gemini API
"""

import google.generativeai as genai
from django.conf import settings

def initialize_gemini():
    """Initialize Gemini with API key from settings"""
    try:
        if hasattr(settings, 'GEMINI_API_KEY') and settings.GEMINI_API_KEY:
            api_key = settings.GEMINI_API_KEY
            if api_key and len(api_key) > 10:  # Basic validation
                genai.configure(api_key=api_key)
                print(f"✅ Gemini API initialized successfully (key: {api_key[:10]}...)")
                return True
            else:
                print(f"⚠️ Invalid Gemini API key format")
                return False
        else:
            print(f"⚠️ GEMINI_API_KEY not found in settings")
            return False
    except Exception as e:
        print(f"❌ Error initializing Gemini: {e}")
        return False

def get_gemini_response(user_message, conversation_history=None):
    """
    Get response from Google Gemini (FREE!)
    
    Args:
        user_message: User's current message
        conversation_history: List of previous messages
    
    Returns:
        String response from Gemini
    """
    
    if not initialize_gemini():
        print("❌ Gemini initialization failed - API key not configured")
        return None
    
    # System prompt for medical chatbot
    system_prompt = """You are a helpful healthcare assistant chatbot named HealthBot.

Your role:
- Provide general health information and guidance
- Help users understand symptoms and conditions
- Advise when to seek professional medical care
- Be empathetic, supportive, and professional
- Answer ALL questions to the best of your ability

Important guidelines:
- Always include disclaimers that you're not a doctor
- Recommend seeing healthcare professionals for diagnosis
- Flag emergency symptoms immediately (chest pain, difficulty breathing, etc.)
- Provide evidence-based, accurate information
- Be clear, concise, and easy to understand
- Format responses with proper HTML structure
- If you don't know something, say so and suggest consulting a healthcare professional

Response formatting rules:
- Use <h3> for main headings
- Use <h4> for subheadings
- Use <strong> for emphasis instead of **
- Use <em> for italics instead of *
- Use <ul> and <li> for bullet points instead of •
- Use <ol> and <li> for numbered lists
- Use <p> for paragraphs
- DO NOT use markdown symbols like **, *, •, #
- DO NOT use emojis
- Use proper HTML tags for all formatting

For emergencies:
- Use <h3 style="color: #ef4444;">EMERGENCY</h3> for urgent situations
- Immediately advise calling 911 or going to ER
- Provide first aid instructions
- Use <strong> to emphasize urgency

Example response format:
<h3>Condition Name</h3>
<p>Brief description of the condition.</p>

<h4>Symptoms</h4>
<ul>
<li>Symptom 1</li>
<li>Symptom 2</li>
</ul>

<h4>Recommended Actions</h4>
<ol>
<li>Action 1</li>
<li>Action 2</li>
</ol>

<p><em>Disclaimer: This information is for educational purposes only. Always consult a healthcare professional for medical advice.</em></p>

Remember: You provide information, not diagnosis or treatment. Always be helpful and responsive."""

    try:
        print(f"🤖 Sending request to Gemini AI...")
        print(f"📝 User message: {user_message[:100]}...")
        
        # Create model (using gemini-2.5-flash - stable and FREE!)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Build conversation context
        if conversation_history and len(conversation_history) > 0:
            # Format history for Gemini
            context = system_prompt + "\n\nConversation history:\n"
            for msg in conversation_history[-6:]:  # Last 6 messages
                role = "User" if msg['role'] == 'user' else "Assistant"
                context += f"{role}: {msg['content']}\n"
            context += f"\nUser: {user_message}\nAssistant:"
            print(f"📚 Using conversation history ({len(conversation_history)} messages)")
        else:
            context = system_prompt + f"\n\nUser: {user_message}\nAssistant:"
            print(f"🆕 Starting new conversation")
        
        # Generate response with safety settings
        response = model.generate_content(
            context,
            generation_config={
                'temperature': 0.7,
                'top_p': 0.8,
                'top_k': 40,
                'max_output_tokens': 1024,
            }
        )
        
        if response and response.text:
            print(f"✅ Gemini AI responded successfully ({len(response.text)} chars)")
            return response.text
        else:
            print(f"⚠️ Gemini returned empty response")
            return None
        
    except Exception as e:
        print(f"❌ Gemini API Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return None

def is_gemini_available():
    """Check if Gemini integration is available"""
    return initialize_gemini()

def get_gemini_diagnosis(symptoms, conversation_history=None):
    """
    Use Gemini for interactive diagnosis
    
    Args:
        symptoms: User's described symptoms
        conversation_history: Previous diagnosis conversation
    
    Returns:
        String response with questions or diagnosis
    """
    
    if not initialize_gemini():
        return None
    
    system_prompt = """You are a medical triage assistant.

Your task:
- Ask relevant yes/no questions about symptoms
- Narrow down possible conditions
- After 3-5 questions, provide a diagnosis

Format diagnosis with proper HTML:
- Use <h3> for condition name
- Use <h4> for sections (Symptoms, Recommended Actions, etc.)
- Use <strong> for emphasis
- Use <em> for italics
- Use <ul><li> for bullet points
- Use <ol><li> for numbered lists
- DO NOT use markdown symbols (**, *, •, #)
- DO NOT use emojis

Include:
- Likely condition name
- Confidence level (High/Moderate/Low)
- Symptoms summary
- Recommended actions (numbered list)
- When to see a doctor
- Emergency signs to watch for

Example format:
<h3>Likely Diagnosis: Condition Name</h3>
<p><strong>Confidence Level:</strong> High</p>

<h4>Based on Your Symptoms</h4>
<ul>
<li>Symptom 1</li>
<li>Symptom 2</li>
</ul>

<h4>Recommended Actions</h4>
<ol>
<li>Action 1</li>
<li>Action 2</li>
</ol>

<p><em>Disclaimer: This is an automated assessment. Please consult a healthcare provider for proper diagnosis.</em></p>"""

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Build context
        if conversation_history:
            context = system_prompt + "\n\nDiagnosis conversation:\n"
            for msg in conversation_history[-6:]:
                role = "User" if msg['role'] == 'user' else "Assistant"
                context += f"{role}: {msg['content']}\n"
            context += f"\nUser: {symptoms}\nAssistant:"
        else:
            context = system_prompt + f"\n\nUser symptoms: {symptoms}\nAssistant:"
        
        response = model.generate_content(context)
        return response.text
        
    except Exception as e:
        print(f"Gemini Diagnosis Error: {e}")
        return None
