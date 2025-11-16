from django.db import models
class Conversation(models.Model):
    session_id = models.CharField(max_length=200, db_index=True)
    user_text = models.TextField()
    bot_text = models.TextField()
    language = models.CharField(max_length=10, default='en')
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.session_id} @ {self.timestamp}"
