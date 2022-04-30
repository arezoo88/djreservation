from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import *


class RoomInLine(NestedStackedInline):
    model = Room
    extra = 1


@admin.register(Hotel)
class HotelInline(NestedModelAdmin):
    model = Hotel
    list_display = ('name', 'address')
    inlines = [
        RoomInLine
    ]
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'room')
