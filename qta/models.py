from django.db import models
from django.utils.timezone import now
from datetime import datetime

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
    
    # Relacionar con los contactos en un modelo separado si es necesario
    contact_number = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=20)
    
    # Relación de seguimientos con un modelo separado
    first_follow_up = models.ForeignKey('FollowUp', on_delete=models.CASCADE, related_name='first_follow_up', blank=True, null=True)
    second_follow_up = models.ForeignKey('FollowUp', on_delete=models.CASCADE, related_name='second_follow_up', blank=True, null=True)
    third_follow_up = models.ForeignKey('FollowUp', on_delete=models.CASCADE, related_name='third_follow_up', blank=True, null=True)
    
    Support_name = models.CharField(max_length=20, blank=True, default="")
    time_finish = models.DateTimeField(null=True, blank=True)
    
    id_unico = models.IntegerField(primary_key=True, unique=True)
    
class FollowUp(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='follow_ups')
    follow_up_time = models.DateTimeField(default=now)
    follow_up_text = models.CharField(max_length=500, blank=True, default="")
    follow_up_type = models.CharField(max_length=50, blank=True, default="")
