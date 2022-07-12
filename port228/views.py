
from django.shortcuts import render

from main_gif.views import main_gif
from .models import Port228
from best_games.models import Best_games
from main_gif.models import Main_gif
def port228(request):
    port228 = Port228.objects.all()
    best_games = Best_games.objects.all()
    main_gif = Main_gif.objects.all()
    context = {
        'port228':port228,
        'best_games':best_games,
        'main_gif':main_gif
    }
    return render(request,'index.html',context)

