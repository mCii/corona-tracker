from django.db.models import Model, ForeignKey, SET_NULL, BooleanField, TextField, CharField

from common.behaviours import Timestampable
from user.models import User, Region


class Case(Timestampable, Model):
    MINOR = 'minor'
    MODERATE = 'moderate'
    SEVERE = 'SEVERE'
    SYMPTOMS_GRAVITY_CHOICES = (
        (MINOR, 'Minor'),
        (MODERATE, 'Moderate'),
        (SEVERE, 'Severe')
    )

    patient = ForeignKey(User, null=True, blank=True, on_delete=SET_NULL)
    location = ForeignKey(Region, on_delete=SET_NULL, null=True, blank=True)
    in_quarantine = BooleanField(default=True)
    is_tested_positive = BooleanField(default=False)
    is_hospitalized = BooleanField(default=False)
    is_dead = BooleanField(default=False)
    is_recovered = BooleanField(default=False)
    symptoms_gravity = CharField(max_length=32, choices=SYMPTOMS_GRAVITY_CHOICES, blank=True, null=True)
    additional_details = TextField(blank=True, null=True)
