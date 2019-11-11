from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    status = models.BooleanField(default=False)