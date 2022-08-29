from django.db import models

# Create your models here.
class workout_model(models.Model):
    day=models.CharField(max_length=100)
    workout_name=models.CharField(max_length=100)
def __str__(self):
    return self.workout_name
