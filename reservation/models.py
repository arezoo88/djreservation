from django.db import models
from django.utils import timezone
from django.forms import ValidationError


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Hotel(BaseModel):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=3000)

    def __str__(self):
        return self.name


class Room(BaseModel):
    ROOM_CATEGORIES = (
        ('Single', 'Single'),
        ('Double', 'Double')
    )
    number = models.IntegerField()
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE)
    category = models.CharField(max_length=6, choices=ROOM_CATEGORIES)
    capacity = models.IntegerField()
    beds = models.IntegerField()

    def __str__(self) -> str:
        return f'pk: {self.pk} , {self.number} in {self.hotel.name} Hotel'


class Booking(BaseModel):
    name = models.CharField(max_length=200)
    room = models.ForeignKey(
        to=Room, on_delete=models.CASCADE, related_name='booking')
    person_count = models.PositiveIntegerField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
