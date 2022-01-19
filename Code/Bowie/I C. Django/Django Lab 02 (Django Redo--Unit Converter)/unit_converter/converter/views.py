from enum import Enum

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class Units(str, Enum):
    meter = "m"
    mile = "mi"
    feet = "ft"
    kilometer = "km"
    yard = "yd"
    inch = "in"

meters_to_unit_rates = {
    Units.meter: 1,
    Units.mile: 0.0006,
    Units.feet: 3.28,
    Units.kilometer: 0.001,
    Units.yard: 1.093,
    Units.inch: 39.37
}

def index(request):
    response_data = {"units": [u.value for u in Units]}
    print(request)
    print(request.method)
    print(request.POST)
    if request.method == "POST":
        input_number = request.POST.get("input_number")
        from_unit = request.POST.get("from")
        to_unit = request.POST.get("to")
        if from_unit == Units.meter:
            result = int(input_number) * meters_to_unit_rates[to_unit]
        else:
            result = (int(input_number) / meters_to_unit_rates[from_unit]) * meters_to_unit_rates[to_unit]
        response_data["result"] = result
    return render(request, "converter/index.html", response_data)
