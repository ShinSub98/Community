from django.urls import path
from . import views
from .views import *

app_name = 'board'

urlpatterns = [
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/comments/', CommentList.as_view()),
    path('<str:univ>/', UnivBoardList.as_view()),
]