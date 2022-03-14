import re
from tkinter import N
from django.shortcuts import redirect,render
from . forms import *       # importing forms model 
from django.contrib import messages #imported messages
from django.views import generic



# Create your views here.
def home(request):
    return render(request,'Dashboard/home.html')       #rendering home file

def notes(request):
    if request.method == 'POST':     #added post method
        form = NotesForm(request.POST)
        if form.is_valid():
            notes= Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes Added from {request.user.username} Successfully!")    
        
    else: 
        form = NotesForm()
    
    notes = Notes.objects.filter(user=request.user)    #created notes object and pass request user that is login user
    context = {'notes':notes,'form':form}         #passing notes object using context
    return render(request,'Dashboard/notes.html',context)      #rendering notes file  #passing context object in file


def delete_note(request,pk=None):         #for deleting notes object used primary key
    Notes.objects.get(id=pk).delete()
    return redirect("notes")


class NotesDetailView(generic.DetailView):
    model = Notes
    



def homework(request):
    form = HomeworkForm()
    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False    
    context={'homeworks':homework,
             'homeworks_done':homework_done,
             'form':form,
            }
    return render(request,'Dashboard/homework.html',context)    

