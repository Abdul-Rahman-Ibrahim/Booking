import json
from datetime import date, timedelta
# pyrefly: ignore [missing-import]
from django.core.serializers.json import DjangoJSONEncoder

# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.views.generic import View

from .models import Equipment, Booking


class HomePageView(View):
    def get(self, request):
        today = date.today()
        view_dates = [today + timedelta(days=i) for i in range(3)]

        week_start = view_dates[0]
        week_end = view_dates[-1]
        
        bookings = Booking.objects.filter(
            start_time__date__gte=week_start,
            start_time__date__lte=week_end,
        ).select_related('user', 'equipment')

        booking_list = json.dumps([
            {
            'equipment_name': b.equipment.name,
            'user_name': b.user.username,
            'start_time': b.start_time.isoformat(),
            'end_time': b.end_time.isoformat(),
            'status': b.status,
        }
        for b in bookings], cls=DjangoJSONEncoder)


        context = {
            'active_page': 'calendar',
            'equipment_list': Equipment.objects.all(),
            'booking_list': booking_list,
            'view_dates': view_dates,
            'today': today,
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