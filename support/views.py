from django.shortcuts import render
from django import forms

# Create your views here.
def support(request):
    return render(request, 'support.html', {})



