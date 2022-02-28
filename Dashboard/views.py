import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Dashboard/home.html')       #rendering home file

def notes(request):
    return render(request,'Dashboard/notes.html')      #rendering notes file
