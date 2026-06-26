# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.views.generic import View

from .models import Equipment


class HomePageView(View):
    def get(self, request):
        context = {
            'active_page': 'calendar',
            'equipment_list': Equipment.objects.all(),
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