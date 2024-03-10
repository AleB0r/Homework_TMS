from django.db import models

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.manufacturer} {self.name} - {self.price}$"