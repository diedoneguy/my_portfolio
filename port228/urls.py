from django.urls import path
from .views import port228

app_name ='port228'
urlpatterns = [
    path('',port228)
]
