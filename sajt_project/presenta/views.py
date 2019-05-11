from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'kontekst': 'jfldkajfls'}
    return render(request, 'presenta/index.html', context=context_dict)
