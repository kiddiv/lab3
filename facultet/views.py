from django.shortcuts import render, get_object_or_404
from pannel.models import Programs
from pannel.models import Departments
from pannel.models import  HomePage
# Create your views here.
def index(request):
    return render(request,'facultet/index.html')

def programs(request):
    programs = Programs.objects.all()
    return render(request, 'facultet/programs.html', {'programs': programs})

def program_detail(request, program_id):
    program = get_object_or_404(Programs, id=program_id)  #і
    return render(request, 'facultet/program_detail.html', {'program': program})

def departments(request):
    departments = Departments.objects.all()
    return render(request, 'facultet/departments.html', {'departments': departments})

def department_detail(request, id):
    department = get_object_or_404(Departments, id=id)
    return render(request, 'facultet/departments_detail.html', {'department': department})

def main_page(request):
    homepage = HomePage.objects.first()
    return render(request, 'facultet/index.html', {'homepage': homepage})
