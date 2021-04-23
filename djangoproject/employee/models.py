from uuid import uuid4

from django.db import models


# Create your models here.
class employee(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=225, blank=True)
    email = models.EmailField(max_length=225)
    job = models.CharField(max_length=225)

    current_date = models.DateTimeField()

    def __str__(self):
        return self.name


class employ(models.Model):
    name = models.CharField(max_length=225)
    mobile_no = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    course = models.CharField(max_length=225)

    def __str__(self):
        return self.name
