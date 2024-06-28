from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('phone number', max_length=100)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.TextField(blank=True, max_length=1000)
    
def __str__(self):
    return self.name