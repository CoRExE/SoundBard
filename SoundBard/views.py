from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
    context = {
        "message": 'Plein de Sons Bientôt !'
    }
    template = loader.get_template('soundbard.index.html')
    return HttpResponse(template.render(context, request))
