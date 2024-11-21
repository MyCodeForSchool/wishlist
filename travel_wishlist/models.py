#This code is used to define the data models/tables that will be used for the database
from django.db import models
from django.contrib.auth.models import User

# Create your models here.  After changing original models, you will need to run migrations.
class Place(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)#Cascade deletes associated data
    name = models.CharField(max_length=200)#constraint set of max 200 characters
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null = True)
    date_visited = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)


    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo'
        notes_str = self.notes [100:] if self.notes else 'no notes'
        return f'{self.name} visited? {self.visited} on {self.date_visited}.  Photo {photo_str}. Notes {notes_str}.'

