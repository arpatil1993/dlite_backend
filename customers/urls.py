from django.urls import path
from . import views

urlpatterns = [
    path('create_new_customer/', views.create_new_customer),
]