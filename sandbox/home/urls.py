from django.contrib.auth.views import LogoutView
from django.urls import path

from sandbox.home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
