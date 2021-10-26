from django.shortcuts import render
from datetime import datetime

import newyears

# Create your views here.

def is_it_newyears(request):
  current_date = datetime.now()
  newyears = False
  if current_date.day == 1 and current_date.month == 1:
    newyears = True
  return render(request, 'newyears/index.html', {
    'newyears': newyears
  })