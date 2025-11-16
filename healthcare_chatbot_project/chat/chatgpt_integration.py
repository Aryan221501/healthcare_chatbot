"""
ChatGPT Integration for Healthcare Chatbot
Provides intelligent, conversational responses using OpenAI's API
"""

import openai
from django.conf import settings

def initialize_openai():
    """Initialize OpenAI with API key from settings"""
    if hasattr(settings, 'OPENAI_API_KEY') and settings.OPENAI_API_KEY:
        openai.api_key = settings.OPENAI_API_KEY
        return True
    return False

def get_chatgpt_response(user_message, conversation_history=None):
    """
    Get response from ChatGPT with medical context
    
    Args:
        user_message: User's current message
        conversation_history: List of previous messages [{"role": "user/assistant", "content": "..."}]
    
    Returns:
        String response from ChatGPT
    """
    
    if not initialize_openai():
        return None
    
    # System prompt for medical chatbot
    system_prompt = """You are a helpful healthcare assistant chatbot named HealthBot.

Your role:
- Provide general health information and guidance
- Help users understand symptoms and conditions
- Advise when to seek professional medical care
- Be empathetic, supportive, and professional
- Use emojis appropriately for better engagement

Important guidelines:
- Always include disclaimers that you're not a doctor
- Recommend seeing healthcare professionals for diagnosis
- Flag emergency symptoms immediately (chest pain, difficulty breathing, etc.)
- Provide evidence-based, accurate information
- Be clear, concise, and easy to understand
- Format responses with bullet points and sections for readability

For emergencies:
- Immediately advise calling 911 or going to ER
- Provide first aid instructions while waiting
- Emphasize urgency with 🚨 emoji

Remember: You provide information and guidance, not diagnosis or treatment.
Always end serious medical advice with a disclaimer."""

    # Build messages array
    messages = [{"role": "system", "content": system_prompt}]
    
    # Add conversation history if available (keep last 10 messages)
    if conversation_history:
        messages.extend(conversation_history[-10:])
    
    # Add current user message
    messages.append({"role": "user", "content": user_message})
    
    try:
        # Call ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Fast and affordable
            messages=messages,
            max_tokens=600,  # Limit response length
            temperature=0.7,  # Balance creativity and consistency
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        return response.choices[0].message.content
        
    except openai.error.AuthenticationError:
        print("ChatGPT API Error: Invalid API key")
        return None
    except openai.error.RateLimitError:
        print("ChatGPT API Error: Rate limit exceeded")
        return "I'm receiving too many requests right now. Please try again in a moment."
    except openai.error.APIError as e:
        print(f"ChatGPT API Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def get_chatgpt_diagnosis(symptoms, conversation_history=None):
    """
    Use ChatGPT for interactive medical diagnosis
    
    Args:
        symptoms: User's described symptoms
        conversation_history: Previous diagnosis conversation
    
    Returns:
        String response with questions or diagnosis
    """
    
    if not initialize_openai():
        return None
    
    system_prompt = """You are a medical triage assistant helping with symptom assessment.

Your task:
- Ask relevant yes/no questions about symptoms
- Narrow down possible conditions systematically
- After 3-5 questions, provide a likely diagnosis

When providing diagnosis, include:
- Likely condition name
- Confidence level (High/Moderate/Low)
- Based on symptoms summary
- Recommended actions (numbered list)
- When to see a doctor
- Emergency signs to watch for
- Expected duration/recovery time

Format questions clearly:
"Question X: [Your question here]"
"Please answer with 'yes' or 'no'."

Format diagnosis with emojis and clear sections."""

    messages = [{"role": "system", "content": system_prompt}]
    
    if conversation_history:
        messages.extend(conversation_history[-10:])
    
    messages.append({"role": "user", "content": symptoms})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"ChatGPT Diagnosis Error: {e}")
        return None

def is_chatgpt_available():
    """Check if ChatGPT integration is available"""
    return initialize_openai()

def get_chatgpt_summary(conversation_history):
    """
    Generate a summary of the conversation
    
    Args:
        conversation_history: List of conversation messages
    
    Returns:
        String summary
    """
    
    if not initialize_openai():
        return None
    
    # Create summary prompt
    conversation_text = "\n".join([
        f"{msg['role']}: {msg['content']}" 
        for msg in conversation_history
    ])
    
    prompt = f"""Summarize this medical conversation in 2-3 sentences:

{conversation_text}

Summary:"""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.5
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"ChatGPT Summary Error: {e}")
        return None
