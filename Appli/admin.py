from django.contrib import admin
from Appli.models import Students


class StudentList(admin.ModelAdmin):  
  list_display = ('name', 'first_name', 'age') 

# Register your models here.
admin.site.register(Students, StudentList)