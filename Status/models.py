from django.db import models

# Create your models here.
class Clock(models.Model):
    time = models.DateTimeField('Time')

class CPU(models.Model):
    percent = models.FloatField('CPU Percent')
    user_times = models.FloatField('User Time')
    temperature = models.IntegerField('CPU Temperature')

class RAM(models.Model):
    total = models.IntegerField('Total Ram')
    percent = models.FloatField('RAM Usage')
    
class Network(models.Model):
    sent = models.IntegerField('Bytes Sent')
    received = models.IntegerField('Bytes Received')