from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Expenses(models.Model):
    description = models.CharField(max_length=255)
    price = models.FloatField()
    date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.price} zł"

 