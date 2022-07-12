from django.urls import path

from best_games.views import best_games

urlpatterns = [
    path('best_games',best_games,name='best_games')
]