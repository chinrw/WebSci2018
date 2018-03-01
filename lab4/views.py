from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'lab4/lab4.html')
