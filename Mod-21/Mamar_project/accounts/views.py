from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import UserRegistrationForm

class registrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy ('register')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) 
