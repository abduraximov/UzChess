from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _


class BaseUser(AbstractUser, BaseModel):
    phone_number = models.CharField(max_length=16, unique=True)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    courses = models.ForeignKey(
        'course.Course',
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name=_('Course')
        )
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} + {self.last_name}'
