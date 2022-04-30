from django.urls import path

from reservation.views import BookingCreateApiView

app_name = 'reservation'

urlpatterns = [
    path('book/', BookingCreateApiView.as_view(), name='BookingApiView')
]
