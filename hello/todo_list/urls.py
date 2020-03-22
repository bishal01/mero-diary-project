from django.urls import path
from . import views

urlpatterns = [
path('base/', views.base, name="base"),
path('delete/<List_id>',views.delete,name="delete"),
path('cross_off/<List_id>',views.cross_off,name="cross_off"),
path('uncross/<List_id>',views.uncross,name="uncross")

]