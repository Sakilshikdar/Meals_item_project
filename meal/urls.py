
from django.urls import path
from  meal import views

urlpatterns = [
    path('',views.meal_home,name='meal_home'),
]