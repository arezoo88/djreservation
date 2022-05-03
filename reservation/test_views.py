from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from reservation.models import *
import json


class BookingCreateApiViewTest(APITestCase):
    fixtures = ["fixtures/db.json"]

    def test_should_not_create_booking_when_before_room_has_been_reserved(self):
        sample_data = {
            "name": "sara",
            "room": 4,
            "person_count": 1,
            "check_in": '2022-06-15T22:22',
            "check_out": '2022-06-17T20:22'
        }
        response = self.client.post(
            reverse('reservation:Booking'), sample_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_should_not_create_booking_when_person_count_is_greather_than_capacity_of_room(self):
        sample_data = {
            "name": "saeed",
            "room": 1,
            "person_count": 44,
            "check_in": '2022-06-15T22:22',
            "check_out": '2022-06-17T20:22'
        }
        response = self.client.post(
            reverse('reservation:Booking'), sample_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class FindAvailableRoomTest(APITestCase):
    fixtures = ["fixtures/db.json"]

    def test_get_all_of_rooms_when_non_of_them_do_not_reserverd_in_period_of_time(self):
        # check db in fixtures/db.json (in db there is 7 rooms)
        response = self.client.get(
            reverse('reservation:AvailRooms'), {'check_in': '2022-07-27T22:22', 'check_out': '2022-09-30T22:22'})
        self.assertEqual(len(json.loads(response.content)), 7)

    def test_should_not_get_rooms_that_are_not_available(self):
        # check db in fixtures/db.json (in db there is 7 rooms but rooms with pk:3,5 in this perid of dates not available)
        response = self.client.get(
            reverse('reservation:AvailRooms'), {'check_in': '2022-06-18T22:22', 'check_out': '2022-06-25T22:22'})
        self.assertEqual(len(json.loads(response.content)), 5)
