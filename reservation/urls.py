from django.urls import path

from reservation.views import BookingCreateApiView, BookingListApiView, find_available_rooms

app_name = 'reservation'

urlpatterns = [
    path('book/', BookingCreateApiView.as_view(), name='Booking'),
    path('booking_list/', BookingListApiView.as_view({'get': 'list'}), name='BookingList'),
    path('avail_rooms/', find_available_rooms, name='AvailRooms')
]
