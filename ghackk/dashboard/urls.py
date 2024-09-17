from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.dash,name="dash"),
    path('newjobsheet/',views.newjobsheet,name="newjobsheet"),
    path('jobdata/<int:id>',views.jobdata,name="jobdata"),
    path('editdata/<int:myid>',views.editdata,name="editdata"),
    path('search/',views.search,name="search"),
    path('delete/<int:myid>',views.delete,name='delete')
    
]