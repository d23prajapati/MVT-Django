from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('employee/', views.employee, name='home'),
    path('details/', views.details, name='home')
]