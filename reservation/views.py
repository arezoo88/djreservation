from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from .utils.availability import check_availability
from .serializers import BookingSerializer


class BookingCreateApiView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        room_number = data.get('room')
        check_in = data.get('check_in')
        check_out = data.get('check_out')
        if check_availability(room_number, check_in, check_out) == True:
            serializer.save()
            return Response(serializer.data)
        else:
            # TODO check status code
            return Response({'success': False, 'msg': 'this room not available'}, status=HTTP_404_NOT_FOUND)
