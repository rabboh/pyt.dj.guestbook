from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Messageboard


def index(request):
    if (request.method == 'POST'):
        nickname = request.POST['nickname']
        email = request.POST['email']
        message = request.POST['message']
        newEntry = Messageboard(nickname=nickname, email=email, message=message)
        newEntry.save()

    entries = Messageboard.objects.all().values()
    context = {
        'entries': entries
    }

    template = loader.get_template('frontend.html')
    return HttpResponse(template.render(context, request))

