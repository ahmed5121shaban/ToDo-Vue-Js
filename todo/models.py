from django.db import models

# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(max_length=500)


    def __str__(self):
        return self.title