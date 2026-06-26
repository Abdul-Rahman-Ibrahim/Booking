# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.views.generic import View 


class HomePageView(View):
    def get(self, request):
        context = {
            'active_page': 'calendar',
        }
        return render(request, 'main/index.html', context)


class EquipmentPageView(View):
    def get(self, request):
        context = {
            'active_page': 'equipment',
        }
        return render(request, 'main/equipment.html')


class SettingsPageView(View):
    def get(self, request):
        context = {
            'active_page': 'settings',
        }
        return render(request, 'main/settings.html')


class BookingListView(View):
    def get(self, request):
        context = {
            'active_page': 'bookings',
        }
        return render(request, 'main/bookings.html')