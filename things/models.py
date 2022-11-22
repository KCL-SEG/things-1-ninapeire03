from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing():
    name = models.CharField(unique=True, max_length=30, blank=False)
    description = models.CharField(unique=False, max_length=120, blank=True)
    quantity = models.PositiveIntegerField(unique=False, validators = [MaxValueValidator(100),MinValueValidator(0)])
