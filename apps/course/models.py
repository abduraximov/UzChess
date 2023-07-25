from django.db import models
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

BEGINNER, AMATEUR, PROFESSIONAL = "Beginner", "Amateur", "Professional"


class Video(BaseModel):
    name = models.CharField(max_length=256)
    video = models.FileField(upload_to="videos", null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    is_completed = models.BooleanField(_('Video is completed'), default=False)

    def __str__(self):
        return self.name


class Chapter(BaseModel):
    name = models.CharField(max_length=256)
    video = models.ForeignKey(
        'course.Video',
        on_delete=models.CASCADE,
        related_name='chaptervideo',
        verbose_name=_('video'))

    def __str__(self):
        return self.name


class Comment(BaseModel):
    user = models.ForeignKey('user.BaseUser',
                             on_delete=models.CASCADE,
                             related_name='user',
                             verbose_name=_('User')
                             )
    course = models.ForeignKey('course.Course',
                               on_delete=models.CASCADE,
                               related_name='course',
                               verbose_name=_('Course')
                               )
    text = RichTextField()
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.user


class Complained(BaseModel):
    name = models.CharField(max_length=256)
    text = RichTextField()
    comment = models.ForeignKey(
        'course.Comment',
        on_delete=models.CASCADE,
        related_name='comment',
        verbose_name=_('Comment')
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Course(BaseModel):
    COURSE_LEVEL = (
        (BEGINNER, _("Boshlang'ich")),
        (AMATEUR, _("Havaskor")),
        (PROFESSIONAL, _("Professional"))
    )

    name = models.CharField(max_length=256)
    author = models.CharField()
    category = models.ForeignKey('course.Category',
                                 on_delete=models.CASCADE,
                                 related_name='category',
                                 verbose_name=_('Category')
                                 )
    level = models.CharField(max_length=32, choices=COURSE_LEVEL)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    views_count = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
