from django.db import models

# Create your models here.
# contact/models.py
from django.db import models

class Visitor(models.Model):
    ip = models.CharField(max_length=50)
    user_agent = models.TextField()
    last_visit = models.DateTimeField(auto_now=True)
