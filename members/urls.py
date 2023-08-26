from django.urls import path
from . import views
from .views import *

app_name = 'members'

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
]