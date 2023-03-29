from django.db import models
from django.contrib.auth import get_user_model
from restaurant.models import Restaurant
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

User = get_user_model()

class Like(models.Model):
    meal = models.ForeignKey('Meal',
    on_delete = models.CASCADE,
    related_name = 'likes',
    verbose_name = _('Meal Likes'),
    )

    user = models.ForeignKey(User,
    on_delete = models.CASCADE,
    related_name = 'likes',
    verbose_name = _('Liked by'),
    )



class Meal(models.Model):
    name = models.CharField(
        max_length = 100,
        blank = False,
        null = False,
        verbose_name = _('Meal name'),
        help_text = _('Required | max-100')
    )

    ingerdiants = models.TextField(
        max_length = 500,
        blank = False,
        null = False,
        verbose_name = _('Meal ingredients'),
        help_text = _('Required | max-500')
    )

    description = models.TextField(
        max_length = 500,
        blank = False,
        null = False,
        verbose_name = _('Meal description'),
        help_text = _('Required | max-500')
    )

    price = models.DecimalField(
        max_digits = 5,
        decimal_places = 2,
        blank = True,
        null = True,
        verbose_name = _('Meal price'),
        help_text = _('Not required  | max-5')
    )
    restaurant = models.ForeignKey(Restaurant,
    on_delete = models.CASCADE,
    related_name = 'meals',
    verbose_name=_('Restaurant who made this meal')
    )

    owner = models.ForeignKey(User,
    on_delete = models.CASCADE,
    related_name = 'meals',
    verbose_name = _('Meal owner'),)

    video = models.FileField(
        upload_to = 'meals/videos/',
        validators = [FileExtensionValidator(
            allowed_extensions = ['mp4', 'mov', 'avi', 'wmv', 'flv', 'mkv'])],
        blank = True,
        null = True,
        verbose_name = _('Meal video'),
        
    )

    no_likes = models.PositiveIntegerField(
        default = 0,
        verbose_name = _('Number of likes'),
        
    )

    def __str__(self):
        return self.name


    @receiver(post_save, sender = Like)
    def update_meal_likes(sender, instance, **kwargs):
        meal = instance.meal
        meal.no_likes = meal.likes.count()
        meal.save()
