// Healthcare Chatbot - Enhanced AJAX implementation with dynamic features
class HealthcareChatbot {
  constructor() {
    this.session = '';
    this.chatWindow = document.getElementById('chatWindow');
    this.form = document.getElementById('chatForm');
    this.input = document.getElementById('textInput');
    this.typingIndicator = null;

    this.init();
  }

  init() {
    this.setupEventListeners();
    this.showWelcomeMessage();

    // Initialize Bootstrap dropdown if available
    if (window.bootstrap && document.getElementById('languageDropdown')) {
      const dropdownElement = document.getElementById('languageDropdown');
      if (dropdownElement) {
        new window.bootstrap.Dropdown(dropdownElement);
      }
    }
  }

  setupEventListeners() {
    // Handle form submission
    this.form.addEventListener('submit', (e) => {
      e.preventDefault();
      this.sendMessage();
    });

    // Handle Enter key for submission (without Shift for new line)
    this.input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        this.sendMessage();
      }
    });

    // Handle input changes for dynamic UI
    this.input.addEventListener('input', () => {
      this.toggleSendButton();
    });

    // Handle language selection
    const languageItems = document.querySelectorAll('.dropdown-item[data-lang]');
    if (languageItems) {
      languageItems.forEach(item => {
        item.addEventListener('click', (e) => {
          e.preventDefault();
          this.selectLanguage(e.target.getAttribute('data-lang'));
        });
      });
    }
  }

  selectLanguage(lang) {
    // Update active language in dropdown
    document.querySelectorAll('.dropdown-item[data-lang]').forEach(item => {
      item.classList.remove('active');
    });
    document.querySelector(`.dropdown-item[data-lang="${lang}"]`).classList.add('active');

    // Add a message about language change
    this.appendMessage('bot', `Language switched to ${lang === 'en' ? 'English' : 'Hindi'}. You can now type in your preferred language.`);
  }

  async sendMessage() {
    const text = this.input.value.trim();
    if (!text) return;

    // Disable send button during processing
    const sendButton = document.getElementById('sendButton');
    sendButton.disabled = true;

    // Add user message to UI with animation
    this.appendMessage('user', text);
    this.input.value = '';
    
    // Reset textarea height
    this.input.style.height = 'auto';

    // Show typing indicator immediately
    this.showTypingIndicator();

    try {
      const response = await this.postMessage(text, this.session);

      // Hide typing indicator immediately when response received
      this.hideTypingIndicator();

      // Store session if provided
      if(response.session) {
        this.session = response.session;
      }

      // Add bot response to UI with proper formatting
      this.appendMessage('bot', response.response);

      // Add smooth scrolling to bottom
      this.scrollToBottom();
    } catch (error) {
      // Hide typing indicator immediately on error
      this.hideTypingIndicator();
      
      // Show detailed error message
      let errorMsg = '⚠️ Error: Could not get response.\n\n';
      if (error.message.includes('Failed to fetch')) {
        errorMsg += '❌ Cannot connect to server. Make sure:\n';
        errorMsg += '1. Django server is running\n';
        errorMsg += '2. You\'re visiting http://127.0.0.1:8000/\n';
        errorMsg += '3. Check the terminal for errors';
      } else if (error.message.includes('403')) {
        errorMsg += '❌ CSRF token error. Try:\n';
        errorMsg += '1. Hard refresh (Ctrl+Shift+R)\n';
        errorMsg += '2. Restart the Django server';
      } else {
        errorMsg += '❌ ' + error.message;
      }
      
      this.appendMessage('bot', errorMsg);
      console.error('Error sending message:', error);
    } finally {
      // Re-enable send button
      this.toggleSendButton();
    }
  }



  async postMessage(text, session = '') {
    const formData = new FormData();
    formData.append('text', text);
    if (session) {
      formData.append('session', session);
    }

    // Get CSRF token if available
    const csrfToken = this.getCsrfToken();

    console.log('Sending message:', text);
    console.log('Session:', session);
    console.log('CSRF Token:', csrfToken ? 'Found' : 'Not found');

    try {
      const response = await fetch('/api/message/', {
        method: 'POST',
        headers: csrfToken ? {
          'X-CSRFToken': csrfToken
        } : {},
        body: formData,
        credentials: 'same-origin'
      });

      console.log('Response status:', response.status);

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error response:', errorText);
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Response data:', data);
      return data;
    } catch (error) {
      console.error('Fetch error:', error);
      throw error;
    }
  }

  getCsrfToken() {
    // Try to get from form first
    const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
    if (csrfInput) {
      return csrfInput.value;
    }
    
    // Fallback to cookie
    const name = 'csrftoken';
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  appendMessage(who, text) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message-container ${who}-message mb-3`;
    messageDiv.style.opacity = '0';

    const bubbleDiv = document.createElement('div');
    bubbleDiv.className = 'message-bubble';
    
    // Format text for better display (handle newlines, etc.)
    const formattedText = this.formatText(text);
    bubbleDiv.innerHTML = formattedText;

    // Add click event to copy message text
    bubbleDiv.addEventListener('click', (e) => {
      if (!window.getSelection().toString()) {
        this.copyMessageText(bubbleDiv);
      }
    });

    // Add timestamp
    const timestamp = document.createElement('small');
    timestamp.className = 'text-muted d-block mt-1';
    timestamp.style.fontSize = '0.75rem';
    timestamp.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    bubbleDiv.appendChild(timestamp);

    messageDiv.appendChild(bubbleDiv);
    this.chatWindow.appendChild(messageDiv);

    // Trigger animation
    requestAnimationFrame(() => {
      messageDiv.style.transition = 'opacity 0.4s ease-out';
      messageDiv.style.opacity = '1';
    });

    // Add smooth scrolling to bottom
    this.scrollToBottom();
  }

  formatText(text) {
    // Replace newlines with <br> tags for proper formatting
    return text.replace(/\n/g, '<br>');
  }

  showTypingIndicator() {
    // Remove any existing typing indicator first
    this.hideTypingIndicator();
    
    this.typingIndicator = document.createElement('div');
    this.typingIndicator.className = 'typing-indicator active bot-message';
    this.typingIndicator.id = 'typingIndicator';

    this.typingIndicator.innerHTML = `
      <div class="typing-indicator-content">
        <div class="d-flex align-items-center mb-2">
          <i class="bi bi-robot me-2 typing-icon"></i>
          <span class="typing-text">Preparing response</span>
          <span class="loading-dots">
            <span></span>
            <span></span>
            <span></span>
          </span>
        </div>
        <div class="typing-progress-bar">
          <div class="typing-progress-fill"></div>
        </div>
      </div>
    `;

    this.chatWindow.appendChild(this.typingIndicator);
    this.scrollToBottom();
  }

  hideTypingIndicator() {
    if (this.typingIndicator) {
      // Remove immediately without animation for faster response
      this.typingIndicator.remove();
      this.typingIndicator = null;
    }
    
    // Also remove any orphaned typing indicators
    const orphanedIndicators = document.querySelectorAll('#typingIndicator, .typing-indicator');
    orphanedIndicators.forEach(indicator => indicator.remove());
  }

  scrollToBottom() {
    // Use smooth scrolling for better UX
    this.chatWindow.scrollTo({
      top: this.chatWindow.scrollHeight,
      behavior: 'smooth'
    });
  }

  toggleSendButton() {
    const sendButton = document.getElementById('sendButton');
    if (this.input.value.trim()) {
      sendButton.disabled = false;
    } else {
      sendButton.disabled = true;
    }
  }

  showWelcomeMessage() {
    // Add initial bot message after a short delay with animation
    setTimeout(() => {
      this.appendMessage('bot', '👋 Hello! I\'m your healthcare assistant. How can I help you today?\n\n💡 You can ask me about:\n• Symptoms (fever, cough, etc.)\n• General health advice\n• Emergency information\n\nFeel free to use the quick action buttons below!');
    }, 800);
  }

  copyMessageText(element) {
    // Extract text without timestamp
    const textContent = element.childNodes[0].textContent + (element.childNodes[1] ? element.childNodes[1].textContent : '');
    const text = textContent.replace(/^(👤|🤖)\s*/, '').trim();
    
    navigator.clipboard.writeText(text).then(() => {
      // Show a brief confirmation with animation
      const checkIcon = document.createElement('i');
      checkIcon.className = 'bi bi-check2-circle ms-2';
      checkIcon.style.color = 'var(--success-color)';
      checkIcon.style.animation = 'fadeIn 0.3s ease-out';
      
      element.appendChild(checkIcon);
      
      setTimeout(() => {
        checkIcon.style.animation = 'fadeOut 0.3s ease-out';
        setTimeout(() => checkIcon.remove(), 300);
      }, 1500);
    }).catch(err => {
      console.error('Failed to copy text: ', err);
      // Show error feedback
      const errorIcon = document.createElement('i');
      errorIcon.className = 'bi bi-x-circle ms-2';
      errorIcon.style.color = 'var(--danger-color)';
      element.appendChild(errorIcon);
      setTimeout(() => errorIcon.remove(), 2000);
    });
  }
}

// Initialize the chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  chatbotInstance = new HealthcareChatbot();
  
  // Add connection status indicator
  window.addEventListener('online', () => {
    showConnectionStatus('online');
  });
  
  window.addEventListener('offline', () => {
    showConnectionStatus('offline');
  });
});

function showConnectionStatus(status) {
  const statusDiv = document.createElement('div');
  statusDiv.className = 'alert alert-' + (status === 'online' ? 'success' : 'warning');
  statusDiv.style.position = 'fixed';
  statusDiv.style.top = '80px';
  statusDiv.style.right = '20px';
  statusDiv.style.zIndex = '9999';
  statusDiv.style.animation = 'fadeInUp 0.4s ease-out';
  statusDiv.innerHTML = `<i class="bi bi-${status === 'online' ? 'wifi' : 'wifi-off'}"></i> ${status === 'online' ? 'Back online' : 'Connection lost'}`;
  
  document.body.appendChild(statusDiv);
  
  setTimeout(() => {
    statusDiv.style.animation = 'fadeOut 0.4s ease-out';
    setTimeout(() => statusDiv.remove(), 400);
  }, 3000);
}

// Global chatbot instance
let chatbotInstance = null;

// Add utility functions for extra features
function clearChat() {
  if (!confirm('Are you sure you want to clear the chat history?')) {
    return;
  }

  const chatWindow = document.getElementById('chatWindow');
  
  // Fade out animation
  chatWindow.style.transition = 'opacity 0.3s ease-out';
  chatWindow.style.opacity = '0';
  
  setTimeout(() => {
    chatWindow.innerHTML = '';
    chatWindow.style.opacity = '1';
    
    // Add a welcome message after clearing
    if (chatbotInstance) {
      chatbotInstance.showWelcomeMessage();
    }
  }, 300);
}

// Quick send function for HTML
function quickSendMessage(message) {
  document.getElementById('textInput').value = message;
  document.getElementById('chatForm').dispatchEvent(new Event('submit'));
}
