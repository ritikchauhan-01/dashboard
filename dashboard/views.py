import time
from datetime import date
from django.shortcuts import redirect
from django.views import generic
from django.template.response import TemplateResponse
from api.models import User
from dashboard.forms import EmployeTypeChoiceForm


class DashBoardView(generic.View):

    # This function will get the data of all the users and send 'api/dashboard' url
    def get(self,request):

        users = User.objects.all()
        if User.is_superuser:          
            items = self.get_context_data(users)
            form = EmployeTypeChoiceForm()
            return TemplateResponse(
                request,
                "dashboard/dashboard.html",
                context={
                    "employees": items,
                    "form": form,
                }
            )
        return ("User is not  Authenticated")


    # This function will  filter out the user w.r.t to their department and send 'api/dashboard' url
    def post(self, request):
        user = request.user
        if user.is_authenticated:
            form = EmployeTypeChoiceForm(request.POST)
            print(form)
            if form.is_valid():
                employee_type = form.cleaned_data["employee_type"]
                users = User.objects.filter(employee_type=employee_type)
                items = self.get_context_data(users)
            return TemplateResponse(
                request,
                "dashboard/dashboard.html",
                context = {
                    "employees": items,
                    "form": form
                },
            )
        return redirect("/admin/")



    # This funtion will get the users details of all the Users from the User model and store it in list and return 
    @staticmethod
    def get_context_data(users):

        employee_details = []
        for user in users:
            employee_details.append({
                "id": user.id,
                "username" : user.username,
                "first_name" : user.first_name,
                "last_name" : user.last_name,
                "email" : user.email,
                "employee_type" : user.employee_type,
                "salary" : user.salary,
                "last_login": user.last_login, 
                "year_of_experience" : 0 if (date.fromtimestamp(time.time()).year - user.date_joined.year)<1
                                    else str(date.fromtimestamp(time.time()).year - user.date_joined.year )+ "."+ str(abs(date.fromtimestamp(time.time()).month - user.date_joined.month)),
            })
        
        return employee_details
            
