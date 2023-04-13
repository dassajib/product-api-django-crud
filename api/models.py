from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    category = models.CharField(max_length=20, blank=False, null=False)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.name;
