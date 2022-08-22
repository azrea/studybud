from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 200) 
    description = models.TextField(null = True, blank=True) 
    # null = true means description is optional blank = true means it can be saved as empty
    #participants
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #auto now add only takes a time stamp on the first save while auto now does it every time the table is updated

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #cascade means that if the room is ever deleted the messages should also be deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]