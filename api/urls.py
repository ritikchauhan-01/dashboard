from django.urls import path
from .views import RegisterationView, LoginView, LogoutView, UserView
from dashboard.views import DashBoardView


urlpatterns = [
    path('dashboard/', DashBoardView.as_view()),
    path('register', RegisterationView),
    path('login',LoginView),
    path('logout', LogoutView),
    path('user', UserView),
]