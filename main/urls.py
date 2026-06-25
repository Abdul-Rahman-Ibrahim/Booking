from django.urls import path # pyrefly: ignore [missing-import]
from .views import HomePageView, EquipmentPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('equipment/', EquipmentPageView.as_view(), name='equipment'),
]
