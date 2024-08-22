from django.db import models

# Create your models here.
class reg(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    class meta():
        db_name="reg"