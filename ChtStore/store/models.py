from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=60, primary_key=True, unique=True)
    price = models.FloatField(default = 0.0)
    inventory_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
