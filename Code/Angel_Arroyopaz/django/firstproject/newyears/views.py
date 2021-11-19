from django.shortcuts import render

from datetime import datetime

# Create your views here.
def is_it_newyears(requests):
    current_date = datetime.now()
    newyears = False

    if current_date.day == 1 and current_date.month == 1:
        newyears = True

    return render(requests, 'newyears/index.html', {
        'newyears': newyears
    })