from django.db import models

class Sale(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')



def __str__(self):
        return self.name
 