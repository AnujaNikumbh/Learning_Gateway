import re
from django.shortcuts import render
from . forms import *       # importing notes model 

# Create your views here.
def home(request):
    return render(request,'Dashboard/home.html')       #rendering home file

def notes(request):
    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)   #created notes object and pass request user that is login user
    context = {'notes':notes}         #passing notes object using context
    return render(request,'Dashboard/notes.html',context)      #rendering notes file  #passing context object in file
