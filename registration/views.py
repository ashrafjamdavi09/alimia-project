from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Registration
from .models import Registration
from .forms import RegistrationForm

class Registration(generic.CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super(Registration, self).form_valid(form)
