from .models import Registration
from django import forms

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['studentfirstname','studentmiddlename','studentlastname','dob','jamaatid','fathersname','studentemailid',
                  'studentphonenumber','homephonenumber','aadharnumber','address1','address2','pincode','city','state','country']
        labels = {'studentfirstname':'First Name', 'studentmiddlename':'Middle Name', 'studentlastname':'Last Name',
                  'dob':'DOB'}
