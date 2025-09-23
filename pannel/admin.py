from django.contrib import admin
from .models import Departments, Programs, Teachers,HomePage
class ProgramsInline(admin.TabularInline):
    model = Programs
    extra = 1
    fields = ('title', 'code', 'coordinator', 'disciplines')
    show_change_link = True

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'head')
    inlines = [ProgramsInline]

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'degree', 'department')
    search_fields = ('full_name',)
    list_filter = ('department',)

@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'department', 'coordinator')
    search_fields = ('title', 'code')
    list_filter = ('department',)
    autocomplete_fields = ('coordinator',)
@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'description')