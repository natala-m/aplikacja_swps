from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PaymentMethod(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    

class Expenses(models.Model):
     
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1 )
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.SET_NULL, null=True, blank=False,default=1)

    def __str__(self):
        return f"{self.category},{self.description} - {self.price} zł"



