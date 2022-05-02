from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import datetime
from reservation.models import *


class BookingCreateApiViewTest(APITestCase):
    fixtures = ["fixtures/db.json"]

    def test_should_not_create_booking_when_before_room_has_been_reserved(self):
        sample_data = {
            "name": "sara",
            "room": 4,
            "capacity": 1,
            "check_in": '2022-06-15T22:22',
            "check_out": '2022-06-17T20:22'
        }
        response = self.client.post(
            reverse('reservation:Booking'), sample_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_should_not_create_booking_when_capacity_is_greather_than_capacity_of_room(self):
        sample_data = {
            "name": "saeed",
            "room": 1,
            "capacity": 44,
            "check_in": '2022-06-15T22:22',
            "check_out": '2022-06-17T20:22'
        }
        response = self.client.post(
            reverse('reservation:Booking'), sample_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
