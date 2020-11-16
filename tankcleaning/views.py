from django.shortcuts import render


# Create your views here.
def tankcleaning(request):
    return render(request, 'tankcleaning.html', {})
