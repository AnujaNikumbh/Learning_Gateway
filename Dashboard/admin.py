from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Notes) #registering notes model       #django admin adds extra s in every table so it will be display as notess
admin.site.register(Homework)
