from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name