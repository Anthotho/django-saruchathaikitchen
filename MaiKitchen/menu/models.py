from django.db import models


class ThaiFoodWarm(models.Model):
    name = models.CharField(max_length=200)
    composition = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    vegan = models.BooleanField(default=False)
    spicy = models.BooleanField(default=False)
    very_spicy = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class ThaiFoodSalad(models.Model):
    name = models.CharField(max_length=200)
    composition = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    vegan = models.BooleanField(default=False)
    spicy = models.BooleanField(default=False)
    very_spicy = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class ThaiFoodDessert(models.Model):
    name = models.CharField(max_length=200)
    composition = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    vegan = models.BooleanField(default=False)
    spicy = models.BooleanField(default=False)
    very_spicy = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'