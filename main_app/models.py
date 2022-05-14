from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SIZES = (
  ('full sized', 'Full Sized'),
  ('1800 compact', '1800 Compact'),
  ('tenkeyless', 'Tenkeyless'),
  ('75%', '75%'),
  ('65%', '65%'),
  ('60%', '60%'),
  ('40%', '40%'),
  ('number pad', 'Number Pad'),
  ('Macro pad', 'Macro Pad'),
)

# Create your models here.
class Keyboard(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    case = models.CharField(max_length=100)
    keycaps = models.CharField(max_length=100)
    switches = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices=SIZES)
    plate = models.CharField(max_length=100, blank=True, null=True)
    stabilizers = models.CharField(max_length=100, blank=True, null=True)
    split = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.case} with {self.switches} switches and {self.keycaps} keycaps'

    def get_absolute_url(self):
      return reverse('detail', kwargs={'keyboard_id': self.id})