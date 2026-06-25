# pyrefly: ignore [missing-import]
from django.shortcuts import render
# pyrefly: ignore [missing-import]
from django.views.generic import View 

# Create your views here.

class CalendarView(View):
    def get(self, request):
        return render(request, 'main/calendar.html')