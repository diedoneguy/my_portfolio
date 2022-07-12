from multiprocessing import context
from django.shortcuts import render
from .models import Best_games
# Create your views here.
def best_games(request):
    best_games = Best_games.objects.all()
    context = {
        'best_games':best_games
    }
    return render(request,'index.html',context)
