from django.urls import path
from .views import RegisterationView, LogoutView, UserView
from dashboard.views import DashBoardView


urlpatterns = [
    path('register', RegisterationView),
    path('logout', LogoutView),
    path('user', UserView),
    path('dashboard', DashBoardView.as_view())
]