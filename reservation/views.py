from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.generics import get_object_or_404
from reservation.models import Booking, Room
from .utils.availability import check_availability
from .serializers import BookingSerializer


class BookingCreateApiView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        room_pk = data.get('room')
        room_obj = get_object_or_404(Room, pk=room_pk)
        if 'capacity' not in data: #TODO handle error format
            return Response({'success': False, 'msg': 'capacity field is mandatory'}, status=HTTP_400_BAD_REQUEST)
        check_in = data.get('check_in')
        check_out = data.get('check_out')
        if check_availability(room_pk, check_in, check_out) == True:
            if room_obj.capacity < data.get('capacity'):
                return Response({'success': False, 'msg': f'maximum capacity is {room_obj.capacity}'}, status=HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        else:
            # TODO check status code
            return Response({'success': False, 'msg': 'this room not available'}, status=HTTP_404_NOT_FOUND)
