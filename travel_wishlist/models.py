#This code is used to define the data models/tables that will be used for the database
from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)#constraint set of max 200 characters
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} visited? {self.visited}'

