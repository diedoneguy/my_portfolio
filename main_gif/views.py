from django.shortcuts import render
from .models import Main_gif
# Create your views here.
def main_gif(requests):
    main_gif = Main_gif.objects.all()
    context = {
        'main_gif':main_gif
    }
    return render(requests,'index.html',context)
