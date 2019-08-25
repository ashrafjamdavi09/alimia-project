from django.shortcuts import render, redirect, get_object_or_404
from .models import Registration
from django.utils import timezone
from jamatSubject.models import Jamaat


def registration(request):
    allJamaat = Jamaat.objects

    if request.method == 'POST':
        newRegistration = Registration()
        newRegistration.studentfirstname = request.POST['fName']
        newRegistration.studentmiddlename = request.POST['mName']
        newRegistration.studentlastname = request.POST['lName']
        newRegistration.dob = request.POST['dob']
        newRegistration.fathersname = request.POST['fathersName']
        newRegistration.studentemailid = "ashrafjamdavi09@outlook.com"
        newRegistration.studentphonenumber = "8881667213"
        newRegistration.homephonenumber = "8881667213"
        newRegistration.aadharnumber = request.POST['aadharID']
        newRegistration.address1 = request.POST['addres1']
        newRegistration.address2 = request.POST['addres2']
        newRegistration.pincode = request.POST['pincode']
        newRegistration.city = request.POST['city']
        newRegistration.state = "UP"
        newRegistration.country = "INDIA"
        selectedJamaat = get_object_or_404(Jamaat, pk=request.POST.get('jamaatid'))
        newRegistration.jamaatid = selectedJamaat
        newRegistration.save()

        return render(request, "registration/afterReg.html", {'info':"saved successfully"})

    else:
        return render(request, 'registration/registration.html', {'allJamaat': allJamaat})
