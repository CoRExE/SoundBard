from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from .models import Student, Sound


# Create your views here.

def index(request):
    context = {
        "message": 'Sound Like a Bard !',
        "student": Student.objects.all()
    }
    template = loader.get_template('Soundbard/soundbard.index.html')
    return HttpResponse(template.render(context, request))


def soundboard_list(request):
    context = {
        'title': 'Sounds List',
        'sounds': Sound.objects.all()
    }
    template = loader.get_template('Soundbard/soundbard.SoundboadList.html')
    return HttpResponse(template.render(context, request))


def upload(request):
    template = loader.get_template('Soundbard/soundbard.upload.html')
    return HttpResponse(template.render({}, request))


def upload_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        myfile = request.FILES['file']
        sound = Sound(title=myfile.name, sound=myfile)
        if Sound.objects.filter(title=sound.title).exists():
            messages.error(request, 'File already exists')
            return soundboard_list(request)
        sound.save()
        messages.success(request, 'File uploaded successfully')
    return soundboard_list(request)


def setting(request):
    return HttpResponse('Setting page')
