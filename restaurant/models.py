from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Create your models here.
User = get_user_model()

class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name = _('Restaurant name'),
        help_text = _('Required | max-100') 
        )
    
    owner = models.ForeignKey(User,
     on_delete=models.CASCADE,
    related_name='restaurants',
    verbose_name = _('Restaurant owner'),
    help_text = _('Required | max-100'))

    address = models.TextField(
        max_length = 500,
        blank = False,
        null = False,
        verbose_name = _('Restaurant address'),
        help_text = _('Required | max-500')
    )

    def __str__(self):
        return self.name