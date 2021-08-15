from django.db import models
from django.urls import reverse


class Cars(models.Model):
    model = models.CharField(max_length=100)
    age = models.IntegerField()
    valume = models.CharField(max_length=100)
    hspeed = models.IntegerField()
    cost = models.CharField(max_length=9)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('prod:detail', args=[self.model])

class Factory(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    cars = models.ManyToManyField('Cars', through='Production')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prod:detail', args=[self.id, self.title])

class Production(models.Model):
    cars = models.ForeignKey('Cars', on_delete=models.CASCADE)
    factory = models.ForeignKey('Factory', on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return self.factory

class Buyer(models.Model):
    name = models.ForeignKey('Cars', on_delete=models.PROTECT)
    surname = models.CharField(max_length=100)
    tel = models.IntegerField()

    def __str__(self):
        return self.surname

class TechPasport(models.Model):
    title = models.OneToOneField('Buyer', on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    valume = models.CharField(max_length=100)
    mass = models.CharField(max_length=3)

    def __str__(self):
        return self.model

