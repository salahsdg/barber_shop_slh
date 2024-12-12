from django.shortcuts import redirect, render

from .forms import AppointmentForm
from .models import Appointment


def index(request):
    return render(request, 'appointments/index.html')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/booking.html', {'form': form})

def success(request):
    return render(request, 'appointments/success.html')
