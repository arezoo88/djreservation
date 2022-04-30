from statistics import mode
from rest_framework import serializers
from .models import Booking


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

    def to_representation(self, instance):
        rep = super(BookingSerializer, self).to_representation(instance)
        rep['room'] = instance.room.number
        return rep
