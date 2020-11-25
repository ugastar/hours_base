from django.db import models

# Create your models here.

class Solicitar1(models.Model):
     startdate=models.DateTimeField('Data Início', null=False, blank=False)

     endate=models.DateTimeField(null=False, blank=False)

     justificate=models.TextField(max_length=2000)

     created=models.DateTimeField(auto_now_add=True)