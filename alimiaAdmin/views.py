from django.shortcuts import render
from registration.models import Registration

def adminHome(request):
    allregistration = Registration.objects
    return render(request, 'alimiaAdmin/adminHome.html')

def regisrations(request):
    allregistration = Registration.objects
    return render(request, 'alimiaAdmin/RegisteredStudents.html', {'allregistration':allregistration})
