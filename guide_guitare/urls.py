from django.urls import path
from .views import index, guitares

urlpatterns = [
    path('', index, name="index"),
    path('guitares', guitares, name="guitares"),
]
