from django.db import models
from django.utils.timezone import now
from datetime import datetime

# Create your models here.
class Ticket(models.Model):
    ticket_number = models.CharField(max_length=20)
    call_time = models.DateTimeField()
    priority = models.CharField(max_length=20)
    discussion = models.CharField(max_length=100)
    
    STATE_CHOICES = [
    ("New", "New"),
    ("In progress", "In progress"),
    ("Completed", "Completed"),
    ]
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default="New")
    place = models.CharField(max_length=20)
    equipment = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=20)
    first_follow_up = models.CharField(max_length=500, blank=True, default="")
    second_follow_up = models.CharField(max_length=500, blank=True, default="")
    third_follow_up = models.CharField(max_length=500, blank=True, default="")
    Support_name = models.CharField(max_length=20, blank=True, default="")
    third_follow_up = models.CharField(max_length=500, default="")
    id_unico = models.IntegerField(primary_key=True)
    time_finish = models.DateTimeField(default=datetime(1, 1, 1, 0, 0, 0))
    