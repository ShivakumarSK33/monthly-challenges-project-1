from django.urls import path
from . import views

urlpatterns = [
    path("<str:home>", views.house, name="house-items")
]
