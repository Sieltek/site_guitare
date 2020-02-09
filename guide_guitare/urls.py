from django.urls import path
from .views import index, guitares, create_guitare, connexion, logout_view

urlpatterns = [
    path('', index, name="index"),
    path('guitares/<int:id_guitare>', guitares, name="guitares"),
    path('create_guitare', create_guitare, name="create_guitare"),
    path('connexion', connexion, name="connexion"),
    path('deconnexion', logout_view, name="logout"),
]
