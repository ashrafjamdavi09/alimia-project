from django.shortcuts import render

def adminHome(request):
    return render(request, 'alimiaAdmin/adminHome.html')
