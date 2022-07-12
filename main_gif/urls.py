from django.urls import path
from .views import main_gif

urlpatterns = [
    path('main_gif',main_gif)
]