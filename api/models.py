from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from todo_auth.models import User



@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'user': self.user.username,
            'completed': self.completed,
            'created_at': datetime.strftime(self.created_at, '%Y-%m-%d %H:%M:%S'),
            'updated_at': datetime.strftime(self.updated_at, '%Y-%m-%d %H:%M:%S'),
        }

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Todos"
        verbose_name = "Todo"
