from asyncore import write
from pyexpat import model
from pkg_resources import require
from rest_framework import serializers
from .models import Booking, Hotel, Room


class BookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"]
    )
    check_out = serializers.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"]
    )

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        if data["check_out"] < data["check_in"]:
            raise serializers.ValidationError({
                "error": "check_in datetime cannot be greater than check_out datetime",
            })

        return super(BookingSerializer, self).validate(data)

    def to_representation(self, instance):
        rep = super(BookingSerializer, self).to_representation(instance)
        rep['room'] = instance.room.number
        rep['capacity'] = instance.room.capacity
        rep['hotel'] = instance.room.hotel
        return rep


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('name', 'address')


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(required=False)
    check_in = serializers.DateTimeField(required=True, write_only=True)
    check_out = serializers.DateTimeField(required=True, write_only=True)

    class Meta:
        model = Room
        fields = '__all__'
        extra_kwargs = {
            "number": {"required": False}, "category": {"required": False}, "capacity": {"required": False}, "beds": {"required": False}
        }

    def validate(self, data):
        if data["check_out"] < data["check_in"]:
            raise serializers.ValidationError({
                "error": "check_in datetime cannot be greater than check_out datetime",
            })
