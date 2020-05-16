from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    date_hired = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
