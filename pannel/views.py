from django.shortcuts import render
from .models import Programs

# Create your views here.
def programs_home(request):
    programs = Programs.objects.all()
    return render(request,'pannel/pannel_home.html',{'programs':programs})