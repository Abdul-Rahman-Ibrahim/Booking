from django.urls import path # pyrefly: ignore [missing-import]
# pyrefly: ignore [missing-import]
from .views import HomePageView, EquipmentPageView, SettingsPageView, BookingListView, FilterEquipmentView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('equipment/', EquipmentPageView.as_view(), name='equipment'),
    path('settings/', SettingsPageView.as_view(), name='settings'),
    path('bookings/', BookingListView.as_view(), name='bookings'),
    path('filter-equipment/', FilterEquipmentView.as_view(), name='filter_equipment'),
]
