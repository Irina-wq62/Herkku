from django.db import models
 
class product(models.Model):
    group = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=300)
    

    

    

    
