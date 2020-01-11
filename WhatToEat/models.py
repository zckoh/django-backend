from django.db import models
from django.utils import timezone

class CookingDish(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added',auto_now_add=True)
    additional_details = models.TextField()
    
    def __str__(self):
        return self.name
