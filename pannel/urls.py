from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.programs_home,name='program_home'),

]
