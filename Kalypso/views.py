import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from .models import Chat
import requests


# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        context = {
            'login': True
        }
    else:
        context = {
            'login': False
        }
    return render(request, 'kalypso/homepage.html', {'login': True})


def install(request):
    return render(request, 'kalypso/installation.html')


def setup(request):
    switch = request.GET.get("setup")
    try:
        if switch == "test":
            requests.get("http://localhost:11434/")
            return JsonResponse({'response': 'Success'})
        elif switch == "installed":
            tags = requests.get("http://localhost:11434/tags")
            return JsonResponse({'response': 'Success', 'tags': tags.json()})
        elif switch == "pull":
            data = requests.post("http://localhost:11434/api/pull",
                                 data=json.dumps({'name': 'llama3'}))
            return JsonResponse(data.json())
    except requests.exceptions.ConnectionError:
        return JsonResponse({'response': 'Error'})
    return HttpResponse("Invalid setup")


def credentials(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigez vers une page de succès.
            return render(request, 'kalypso/homepage.html', {'login': True})
        else:
            # Retournez une erreur 'invalid login'
            return HttpResponse("Invalid login")
    elif request.GET.get('credential'):
        ctx = {
            'credential': 'login',
        }
        return render(request, 'kalypso/credentials.html', ctx)
    else:
        # Affichez la page de sign up
        return render(request, 'kalypso/credentials.html')


def quick_chat(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        message = request.GET.get('message', None)
        if message is None:
            return JsonResponse({'response': 'Error'})
        data = requests.post(
            'http://localhost:11434/api/generate',
            data=json.dumps({'model': "llama3", 'prompt': message, 'stream': False})
        )
        data = json.loads(data.text)
        return JsonResponse(data) if data.get('response') else JsonResponse({'response': 'Error'})
