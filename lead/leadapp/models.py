from django.db import models
from datetime import datetime,date
# Create your models here.
class batch(models.Model):
    batchname=models.CharField(max_length=10)
    def __str__(self):
        return self.batchname
class details(models.Model):
    batchname=models.ForeignKey(batch,on_delete=models.CASCADE,)
    course = models.CharField(max_length=30)
    trainer = models.CharField(max_length=30)
    Start_date = models.DateField()
    End_date = models.DateField()
    def __str__(self):
        return self.course, trainer, Start_date, End_date
