from django.db import models
import uuid

class Lesson(models.Model):
    lesson_id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    banner = models.CharField(max_length=255)
    rating = models.FloatField(max_length=255)
    
    def __str__(self):
        return self.title