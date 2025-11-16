# 🤖 ChatGPT Integration Guide

## Overview
You can integrate OpenAI's ChatGPT API into your healthcare chatbot to make it more intelligent, conversational, and capable of understanding complex queries.

---

## 🎯 Benefits of ChatGPT Integration

### Current System (Rule-Based):
- ❌ Limited to predefined responses
- ❌ Can't understand complex questions
- ❌ No conversational context
- ❌ Rigid keyword matching

### With ChatGPT:
- ✅ Natural language understanding
- ✅ Conversational responses
- ✅ Context awareness
- ✅ Handles complex medical queries
- ✅ More human-like interactions
- ✅ Can explain medical concepts
- ✅ Adapts to user's language style

---

## 📋 Prerequisites

### 1. OpenAI API Key
- Sign up at: https://platform.openai.com/
- Go to API Keys section
- Create new API key
- **Cost:** Pay-as-you-go (very affordable for chatbots)
  - GPT-3.5-turbo: ~$0.002 per 1K tokens
  - GPT-4: ~$0.03 per 1K tokens

### 2. Install OpenAI Python Library
```bash
pip install openai
```

---

## 🔧 Implementation Steps

### Step 1: Install Required Package
```bash
cd healthcare_chatbot_project
pip install openai
```

### Step 2: Update requirements.txt
Add to `requirements.txt`:
```
openai>=1.0.0
```

### Step 3: Store API Key Securely
Create `.env` file in project root:
```bash
# .env
OPENAI_API_KEY=your-api-key-here
```

Install python-dotenv:
```bash
pip install python-dotenv
```

Add to requirements.txt:
```
python-dotenv>=1.0.0
```

### Step 4: Update settings.py
```python
# healthcare/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
```

### Step 5: Create ChatGPT Integration Module
Create `chat/chatgpt_integration.py`:

```python
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def get_chatgpt_response(user_message, conversation_history=None):
    """
    Get response from ChatGPT with medical context
    """
    
    # System prompt for medical chatbot
    system_prompt = '''You are a helpful healthcare assistant chatbot. 
    
Your role:
- Provide general health information and guidance
- Help users understand symptoms and conditions
- Advise when to seek professional medical care
- Be empathetic and supportive

Important guidelines:
- Always include disclaimers that you're not a doctor
- Recommend seeing healthcare professionals for diagnosis
- Flag emergency symptoms immediately
- Provide evidence-based information
- Be clear, concise, and easy to understand
- Use emojis appropriately for better engagement

For emergencies (chest pain, difficulty breathing, etc.):
- Immediately advise calling 911
- Provide first aid instructions
- Emphasize urgency

Remember: You provide information, not diagnosis or treatment.'''

    # Build messages array
    messages = [{"role": "system", "content": system_prompt}]
    
    # Add conversation history if available
    if conversation_history:
        messages.extend(conversation_history)
    
    # Add current user message
    messages.append({"role": "user", "content": user_message})
    
    try:
        # Call ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" for better quality
            messages=messages,
            max_tokens=500,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"ChatGPT API Error: {e}")
        return "I'm having trouble connecting right now. Please try again in a moment."

def get_chatgpt_diagnosis(symptoms, conversation_history=None):
    """
    Use ChatGPT for interactive diagnosis
    """
    
    system_prompt = '''You are a medical triage assistant. 
    
Your task:
- Ask relevant yes/no questions about symptoms
- Narrow down possible conditions
- Provide likely diagnosis with confidence level
- Give treatment recommendations
- Advise when to seek medical care

Format your questions clearly and ask one at a time.
After 3-5 questions, provide a diagnosis with:
- Likely condition
- Confidence level (High/Moderate/Low)
- Recommended actions
- When to see a doctor
- Emergency signs to watch for'''

    messages = [{"role": "system", "content": system_prompt}]
    
    if conversation_history:
        messages.extend(conversation_history)
    
    messages.append({"role": "user", "content": symptoms})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=400,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"ChatGPT API Error: {e}")
        return None
```

### Step 6: Update views.py
```python
# chat/views.py
from .chatgpt_integration import get_chatgpt_response
from django.conf import settings

# Store conversation history (use database in production)
conversation_histories = {}

def message_api(request):
    if request.method == 'POST':
        try:
            text = request.POST.get('text', '').strip()
            session = request.POST.get('session', '') or str(uuid.uuid4())
            
            # Check if ChatGPT is enabled
            if settings.OPENAI_API_KEY:
                # Get conversation history
                history = conversation_histories.get(session, [])
                
                # Get ChatGPT response
                response = get_chatgpt_response(text, history)
                
                # Update conversation history
                history.append({"role": "user", "content": text})
                history.append({"role": "assistant", "content": response})
                
                # Keep only last 10 messages (5 exchanges)
                conversation_histories[session] = history[-10:]
            else:
                # Fallback to rule-based system
                lang = detect_language(text)
                response = match_kb(lang, text)
            
            # Save to database
            try:
                Conversation.objects.create(
                    session_id=session,
                    user_text=text,
                    bot_text=response,
                    language='en'
                )
            except Exception as db_error:
                print(f"Database error: {db_error}")
            
            return JsonResponse({
                'session': session,
                'response': response,
                'language': 'en',
                'powered_by': 'chatgpt' if settings.OPENAI_API_KEY else 'rules'
            })
            
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'POST required'}, status=400)
```

---

## 🎨 Hybrid Approach (Best of Both Worlds)

Combine rule-based and ChatGPT:

```python
def message_api(request):
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        session = request.POST.get('session', '') or str(uuid.uuid4())
        
        # Check for emergencies first (rule-based)
        if is_emergency(text):
            response = get_emergency_response()
        
        # Check if user wants diagnosis
        elif 'diagnose' in text.lower():
            response = start_diagnosis(session, text)
        
        # Use ChatGPT for general queries
        elif settings.OPENAI_API_KEY:
            history = conversation_histories.get(session, [])
            response = get_chatgpt_response(text, history)
            
            # Update history
            history.append({"role": "user", "content": text})
            history.append({"role": "assistant", "content": response})
            conversation_histories[session] = history[-10:]
        
        # Fallback to rule-based
        else:
            lang = detect_language(text)
            response = match_kb(lang, text)
        
        return JsonResponse({
            'session': session,
            'response': response,
            'language': 'en'
        })
```

---

## 💰 Cost Estimation

### GPT-3.5-turbo (Recommended for chatbots):
- **Cost:** ~$0.002 per 1K tokens
- **Average conversation:** ~500 tokens
- **Cost per conversation:** ~$0.001 (0.1 cents)
- **1000 conversations:** ~$1
- **Very affordable!**

### GPT-4 (Higher quality):
- **Cost:** ~$0.03 per 1K tokens
- **Average conversation:** ~500 tokens
- **Cost per conversation:** ~$0.015 (1.5 cents)
- **1000 conversations:** ~$15

### Tips to Reduce Costs:
1. Use GPT-3.5-turbo instead of GPT-4
2. Limit max_tokens (e.g., 500)
3. Keep conversation history short (last 10 messages)
4. Use rule-based for simple queries
5. Cache common responses

---

## 🔒 Security Best Practices

### 1. Never Commit API Keys
Add to `.gitignore`:
```
.env
*.env
```

### 2. Use Environment Variables
```python
import os
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
```

### 3. Rate Limiting
```python
from django.core.cache import cache

def check_rate_limit(session):
    key = f"rate_limit_{session}"
    count = cache.get(key, 0)
    if count > 20:  # 20 messages per hour
        return False
    cache.set(key, count + 1, 3600)  # 1 hour
    return True
```

### 4. Input Validation
```python
def validate_input(text):
    if len(text) > 500:
        return False
    if contains_malicious_content(text):
        return False
    return True
```

---

## 🎯 Advanced Features

### 1. Conversation Memory
Store in database:
```python
class ConversationHistory(models.Model):
    session_id = models.CharField(max_length=100)
    role = models.CharField(max_length=20)  # user/assistant
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
```

### 2. Streaming Responses
For real-time typing effect:
```python
def stream_chatgpt_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[...],
        stream=True
    )
    
    for chunk in response:
        if chunk.choices[0].delta.get("content"):
            yield chunk.choices[0].delta.content
```

### 3. Function Calling
Let ChatGPT trigger specific actions:
```python
functions = [
    {
        "name": "book_appointment",
        "description": "Book a doctor appointment",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {"type": "string"},
                "specialty": {"type": "string"}
            }
        }
    }
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions
)
```

---

## 📊 Comparison

### Rule-Based (Current):
**Pros:**
- ✅ Free
- ✅ Fast
- ✅ Predictable
- ✅ No API dependency

**Cons:**
- ❌ Limited understanding
- ❌ Rigid responses
- ❌ Can't handle complex queries
- ❌ No conversation context

### ChatGPT Integration:
**Pros:**
- ✅ Natural conversations
- ✅ Understands context
- ✅ Handles complex queries
- ✅ More human-like
- ✅ Continuously improving

**Cons:**
- ❌ Costs money (but very cheap)
- ❌ Requires API key
- ❌ Slight latency
- ❌ Needs internet connection

### Hybrid (Recommended):
**Pros:**
- ✅ Best of both worlds
- ✅ Cost-effective
- ✅ Reliable fallback
- ✅ Emergency handling

---

## 🚀 Quick Start

### 1. Get API Key
```
1. Go to https://platform.openai.com/
2. Sign up / Log in
3. Go to API Keys
4. Create new key
5. Copy the key
```

### 2. Set Up Environment
```bash
# Create .env file
echo "OPENAI_API_KEY=your-key-here" > .env

# Install packages
pip install openai python-dotenv

# Update requirements.txt
echo "openai>=1.0.0" >> requirements.txt
echo "python-dotenv>=1.0.0" >> requirements.txt
```

### 3. Test Integration
```python
# Test in Python shell
from chat.chatgpt_integration import get_chatgpt_response

response = get_chatgpt_response("I have a fever")
print(response)
```

### 4. Deploy
```bash
python manage.py runserver
```

---

## 🎉 Result

With ChatGPT integration, your chatbot becomes:
- 🧠 **Intelligent** - Understands natural language
- 💬 **Conversational** - Maintains context
- 🎯 **Accurate** - Better medical information
- 🤝 **Helpful** - More human-like interactions
- 🚀 **Scalable** - Handles any query

**Your chatbot will feel like talking to a real healthcare assistant!**

---

## 📝 Next Steps

1. Get OpenAI API key
2. Install required packages
3. Create chatgpt_integration.py
4. Update views.py
5. Test with simple queries
6. Deploy and monitor costs
7. Optimize based on usage

**Want me to implement this for you? Just let me know!** 🚀
