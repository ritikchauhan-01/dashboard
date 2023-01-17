from django.contrib import admin

from .models import User
# from dashboard.forms import EmployeTypeChoiceForm

# class PersonAdmin(admin.ModelAdmin):
#     form = EmployeTypeChoiceForm

# Register your models here.
admin.site.register(User)


