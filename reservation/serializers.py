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

    def validate(self, data):
        if data["check_out"] < data["check_in"]:
            raise serializers.ValidationError({
                "error": "check_in datetime cannot be greater than check_out datetime",
            })

        return super(BookingSerializer, self).validate(data)

    def to_representation(self, instance):
        rep = super(BookingSerializer, self).to_representation(instance)
        rep['room'] = instance.room.number
        return rep
