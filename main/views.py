# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.views.generic import View 

# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'main/index.html')


class EquipmentPageView(View):
    def get(self, request):
        return render(request, 'main/equipment.html')


class SettingsPageView(View):
    def get(self, request):
        return render(request, 'main/settings.html')


class BookingListView(View):
    def get(self, request):
        return render(request, 'main/bookings.html')