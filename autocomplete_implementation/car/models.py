from django.db import models

# Create your models here.


class Car(models.Model):
    name=models.CharField(max_length=20)
  
    model=models.CharField(max_length=20)
    fuel=models.CharField(max_length=10,choices=(('petrol', 'petrol'), ('diesel', 'diesel')))
   
    def __str__(self):
        return self.name