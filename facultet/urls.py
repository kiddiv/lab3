from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.main_page,name='main_page'),
   path('programs',views.programs,name='program_page'),
   path('programs/<int:program_id>/', views.program_detail, name='program_detail'),
   path('departments/', views.departments, name='department_page'),
   path('departments/<int:id>/', views.department_detail, name='department_detail'),

]
