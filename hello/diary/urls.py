from django.urls import path
from . import views


urlpatterns = [
path('ok/', views.ok, name="ok"),
path('add/', views.add, name="add"),
path('view/', views.view, name="view"),
path('calculator/', views.calulator, name="calculator"),
path('calender/', views.calender, name="calender"),
path('games/', views.games, name="games"),








]