from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.contact_name
    
class Room(models.Model):
    room_id = models.CharField(max_length=50)
    user1 = models.CharField(max_length=50)
    user2 = models.CharField(max_length=50)

class Message(models.Model):
    receiver = models.CharField(max_length=50)
    sender = models.CharField(max_length=50)
    message = models.TextField()
    time_stamp = models.DateField()

    def __str__(self):
        return f"{str(self.receiver)} - {self.sender}"