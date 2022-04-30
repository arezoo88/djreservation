from reservation.models import Booking


def check_availability(room, check_in, check_out):
    available_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            available_list.append(True)
        else:
            available_list.append(True)
    return all(available_list)
