from django.db import models

class Goods(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

class Purchase(models.Model):
    goods = models.ForeignKey(Goods)
    number = models.IntegerField()
    date = models.DateTimeField('date purchased')