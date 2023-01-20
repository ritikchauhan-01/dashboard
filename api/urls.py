from django.urls import path
from .views import RegisterationView, LoginView, LogoutView, UserView


urlpatterns = [
    path('register', RegisterationView),
    path('login', LoginView),
    path('logout', LogoutView),
    path('user', UserView),
]
