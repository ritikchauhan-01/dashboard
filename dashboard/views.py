import datetime
from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from api.models import User
# Create your views here.

class DashBoardView(APIView):

    def get(self, request):
        if user.is_superuser:
            employee_details = []
            users = User.objects.all()
            for user in users:
                date = user.date_joined - datetime.date.today()
                print(date)
                content = {
                    "username" : user.username,
                    "first_name" : user.first_name,
                    "last_name" : user.last_name,
                    "email" : user.email,
                    "department" : user.department,
                    "salary" : user.salary,
                    "last_login": user.last_login, 
                    "year_of_experience" : user.date_joined - datetime.date.today()
                }
                employee_details.append(content)
            return employee_details
        
        return ("User is not  Authenticated")



    def post(self,request):
        pass
