from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=50, default = '')
    add = models.CharField(max_length=50, default = '')
    email= models.CharField(max_length=50, default = '')
    phone =models.CharField(max_length=50, default = '')
    password = models.CharField(max_length=50, default='')
    cnfrmpass = models.CharField(max_length=50, default='')
    #id = models.AutoField(auto_created=True, primary_key=True, serialize=False, default='')

