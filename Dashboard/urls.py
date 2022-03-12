from django.urls import path
from . import views                 #importing views in current application using dot

urlpatterns =[
    path('',views.home, name="home") ,            #mapping views.home function 
    path('notes',views.notes,name="notes"),       #mapping views.notes function
    path('delete_note/<int:pk>', views.delete_note, name="delete-note"),#mapping views.delete_note function
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name="notes-detail"),#mapping views.notes_detail function
    
    path('homework', views.homework, name="homework"),
]
