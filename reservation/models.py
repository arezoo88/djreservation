from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=3000)


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('Single','Single'),
        ('Double','Double')
    )
    number = models.IntegerField()
    hotel = models.ForeignKey(to=Hotel,on_delete=models.CASCADE)
    category = models.CharField(max_length=6,choices=ROOM_CATEGORIES)
    capacity  = models.IntegerField()
    beds = models.IntegerField()


class Book(models.Model):
    name = models.CharField(max_length=200)
    room = models.ForeignKey(to=Room,on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()