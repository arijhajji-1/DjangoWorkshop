from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
# Create your models here.
from users.models import*
def titleValidator(value):
    if not value.istitle():
        raise ValidationError('Title must be in title case')
def dateValidator(value):
    if value < datetime.now().date():
        raise ValidationError(' you must insert a new date')
class Event(models.Model):
    CATEGORY_CHOICES = (
        ('Music', 'Music'),
        ('Cinema', 'Cinema'),
        ('Sport', 'Sport'),
    )

    title = models.CharField(max_length=255, null=True, validators=[titleValidator])
    description = models.TextField()
    eventImage = models.ImageField(upload_to='images/', blank=True)

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=8)
    state = models.BooleanField(default=False)
    nbrParticipants = models.IntegerField(default=0)
    eventDate = models.DateField(validators=[dateValidator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizers = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='organizers')


