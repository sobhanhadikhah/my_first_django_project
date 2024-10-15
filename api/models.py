from django.db import models
from django.utils import timezone
class Blog(models.Model):
    title = models.CharField(max_length=200,default="untitled")  # Remove the comma
    content = models.TextField(default="")  # Remove the comma
    created_at = models.DateTimeField(default=timezone.now) # Remove the comma
    updated_at = models.DateTimeField(auto_now=True)  # Remove the comma
    
    def __str__(self):
        return self.title  # This is correct