import json
from datetime import date, timedelta
# pyrefly: ignore [missing-import]
from django.utils.timezone import localtime
# pyrefly: ignore [missing-import]
from django.core.serializers.json import DjangoJSONEncoder

# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.views.generic import View

from .models import Equipment, Booking


class HomePageView(View):
    def get(self, request):
        # Optimized query using select_related to avoid N+1 database hits
        bookings = Booking.objects.select_related("user", "equipment").all()

        booking_list = json.dumps([
            {
                "id": b.id,
                # Store structural text inside extendedProps for clean frontend rendering
                "title": f"{b.user.username} - {b.equipment.name}",
                "start": localtime(b.start_time).isoformat(),
                "end": localtime(b.end_time).isoformat(),
                "backgroundColor": b.equipment.color or "#7c3aed",
                "borderColor": b.equipment.color or "#7c3aed",
                "extendedProps": {
                    "equipmentName": b.equipment.name,
                    "equipmentId": b.equipment.id,
                    "userName": b.user.username,
                    "status": getattr(b, 'status', 'confirmed'),
                }
            }
            for b in bookings
        ], cls=DjangoJSONEncoder)

        context = {
            'active_page': 'calendar',
            'equipment_list': Equipment.objects.all(),
            'booking_list': booking_list,
        }
        return render(request, 'main/index.html', context)


class EquipmentPageView(View):
    def get(self, request):
        context = {
            'active_page': 'equipment',
            'equipment_list': Equipment.objects.all(),
        }
        return render(request, 'main/equipment.html', context)


class SettingsPageView(View):
    def get(self, request):
        context = {
            'active_page': 'settings',
        }
        return render(request, 'main/settings.html', context)


class BookingListView(View):
    def get(self, request):
        context = {
            'active_page': 'bookings',
        }
        return render(request, 'main/bookings.html', context)