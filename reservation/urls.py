from django.urls import path

from reservation.views import BookingCreateApiView, BookingListApiView

app_name = 'reservation'

urlpatterns = [
    path('book/', BookingCreateApiView.as_view(), name='Booking'),
    path('booking_list/', BookingListApiView.as_view({'get': 'list'}), name='BookingList')
]
