from django.db import models

# Create your models here.
class ContactManager(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone_number=models.CharField(max_length=10)
    notes=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
    
    