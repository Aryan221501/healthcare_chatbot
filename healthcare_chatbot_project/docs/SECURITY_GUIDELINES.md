# Security Best Practices Guide

## 🔐 API Key Security

### DOs:
- Store API keys in environment variables, never in code
- Use `.env` files for local development (and add them to `.gitignore`)
- Create `.env.example` files with placeholder values for documentation
- Use Django's `os.getenv()` method to retrieve keys from environment
- Regularly rotate API keys
- Use different keys for development and production environments

### DON'Ts:
- ❌ Never commit actual API keys to version control
- ❌ Never hardcode API keys in source code
- ❌ Never share API keys in documentation files
- ❌ Never use the same API key across multiple repositories without proper management

## 🛡️ Recommended Security Measures

### 1. Environment Configuration
```
# .env file (should be in .gitignore)
GEMINI_API_KEY=your_actual_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# .env.example file (can be committed)
GEMINI_API_KEY=your_actual_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. Update .gitignore
Make sure your `.gitignore` file contains:
```
# Environment variables
.env
.env.local
.env.*.local

# API Keys
*API_KEY*
*api_key*
*.key
*.secret
```

### 3. Code Best Practices
```python
# ✅ Good - retrieve from environment
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

# ❌ Bad - hardcoded key
API_KEY = "AIzaSyC3ES3HHhIv0ALx_xMhBxm1vy8xghRcW54"
```

## 🚨 Incident Response

### If an API key is accidentally exposed:
1. **Immediate action**: Revoke the exposed key from the service provider (Google AI Studio, OpenAI, etc.)
2. **Update code**: Replace the exposed key with a new one
3. **Scan repository**: Search for any other instances of the key
4. **Update documentation**: Ensure no documentation contains the old key
5. **Security audit**: Review all files to ensure complete removal

### Git history cleanup (if needed):
```bash
# Remove sensitive data from git history
git filter-branch --force --index-filter \
"git rm --cached --ignore-unmatch PATH-TO-YOUR-FILE" \
--prune-empty --tag-name-filter cat -- --all

# Or use git rebase to remove commits containing sensitive data
```

## 🔍 Regular Security Checks

### 1. Pre-commit hooks
Consider implementing pre-commit hooks to scan for API keys before commits:
- Install `truffleHog` or `git-secrets`
- Set up automated scanning tools

### 2. File audit
Periodically run:
```bash
# Search for potential API keys in codebase
grep -r "AIza" .
grep -r "sk-" . # OpenAI keys
grep -r "key=" .
```

## 📋 Checklist for Contributions

Before committing changes:
- [ ] Check that no API keys are in the code
- [ ] Verify `.env` and similar files are in `.gitignore`
- [ ] Ensure documentation uses placeholder values only
- [ ] Update `.env.example` if new variables are added
- [ ] Test that project works with example configuration

## 📚 Additional Resources

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [Google Cloud Security Best Practices](https://cloud.google.com/docs/security/best-practices)
- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)

---

**Note**: This guide should be updated whenever new security measures are implemented or when new types of sensitive data are introduced to the project.