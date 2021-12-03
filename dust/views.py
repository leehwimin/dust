from django.shortcuts import render
from .api import check_air

def index(request):
    res = check_air()
    pm10 = res.get('용산구')
    context = {'station': '용산구', 'pm10': pm10}
    return render(request, 'dust/dust_main.html', context)

def detail(request):
    res = check_air()
    context = {'dust': res}
    return render(request, 'dust/dust_detail.html', context)