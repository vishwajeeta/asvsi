import datetime
from django.db import models
from sqlalchemy import true

# Create your models here.

class Notedata(models.Model):
    content=models.TextField(max_length=5000)
    dates=models.DateTimeField(default=datetime.datetime.now)
    class Meta:
        db_table="Note"