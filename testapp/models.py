from django.db import models

class Person(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=64)
    salary = models.FloatField()
    city = models.CharField(max_length=64)

    def __str__(self):
        return self.name
