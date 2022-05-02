from pyexpat import model
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.generics import get_object_or_404
from reservation.models import Booking, Room
from .utils.availability import check_availability
from .serializers import BookingSerializer, RoomSerializer
from weasyprint import CSS, HTML
from django.template.loader import render_to_string
from django.http.response import HttpResponse
import tempfile
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
from django.db.models import Q


class BookingCreateApiView(generics.CreateAPIView):
    """
    This Api use for booking Rooms.

        ---
            parameters:
            - name: name
            description: name (any string)
            required: true
            type: string
            paramType: body
            - name: room
            description: pk of room
            required: true
            type: integer
            paramType: body
            - name: person_count
            description: number of person
            required: true
            type: integer
            paramType: body
            - name: check_in
            description: date and time
            required: true
            type: "%Y-%m-%dT%H:%M"
            paramType: body
            - name: check_out
            description: date and time
            required: true
            type: "%Y-%m-%dT%H:%M"
            paramType: body

    """
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        room_pk = data.get('room')
        room_obj = get_object_or_404(Room, pk=room_pk)
        check_in = data.get('check_in')
        check_out = data.get('check_out')
        if check_availability(room_pk, check_in, check_out) == True:
            if room_obj.capacity < int(data.get('person_count')):
                return Response({'success': False, 'msg': f'maximum capacity is {room_obj.capacity}'}, status=HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        else:
            # TODO check status code
            return Response({'success': False, 'msg': 'this room not available'}, status=HTTP_404_NOT_FOUND)


class BookingListApiView(viewsets.ModelViewSet):
    """
    The listing owner can get an overview over the booked rooms as an HTML or PDF report.

        ---
            parameters:
            - name: user
            description: pk of hotel
            required: true
            type: integer
            in: query
    """
    serializer_class = BookingSerializer
    # permission_classes = (IsAuthenticated,)
    user = openapi.Parameter('user', in_=openapi.IN_QUERY,
                             description='this is hotel_id', type=openapi.TYPE_INTEGER)

    def get_queryset(self):
        # (if there is authentication system,hotel must log in and get hotel_id from request.user but now get the name of hotel from queryparams)
        user = self.request.query_params.get('user')
        if user:
            booking_list = Booking.objects.filter(room__hotel__pk=user)
        else:
            booking_list = Booking.objects.all()

        serializer = self.get_serializer(booking_list, many=True)
        return serializer.data

    @swagger_auto_schema(
        manual_parameters=[user],
    )
    def list(self, request, *args, **kwargs):
        html_string = render_to_string(
            'booking_list.html', {'booking_list': self.get_queryset()})
        html = HTML(string=html_string,
                    base_url=self.request.build_absolute_uri())
        css = CSS(filename='templates/booking_list.css')
        result = html.write_pdf(stylesheets=[css])
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=booking_list.pdf'
        response['Content-Transfer-Encoding'] = 'base64'

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())

        return response


@api_view(['GET'])
def find_available_rooms(request):
    """
    This Api use for get_availble Rooms in define datetime.

        ---
            parameters:
            - name: check_in
            description: date and time
            required: true
            type: "%Y-%m-%dT%H:%M"
            paramType: query
            - name: check_out
            description: date and time
            required: true
            type: "%Y-%m-%dT%H:%M"
            paramType: query

    """
    serializer = RoomSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    check_in = request.query_params.get('check_in')
    check_out = request.query_params.get('check_in')
    booking_list = list(Booking.objects.filter(
        Q(check_out__gte=check_in) & Q(check_in__lte=check_out)).values_list('room', flat=True))
    available_rooms = Room.objects.filter(~Q(pk__in=booking_list))
    return Response(RoomSerializer(available_rooms, many=True).data)
