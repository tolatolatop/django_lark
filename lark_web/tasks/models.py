from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class TaskTmpl(models.Model):
    alias = models.CharField(max_length=255)
    input = models.JSONField()


class Task(models.Model):
    input = models.JSONField()
    status = models.CharField(max_length=2, default='C')
    progress = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    output = models.JSONField(default=dict)
    created_time = models.DateTimeField(auto_now_add=True)
