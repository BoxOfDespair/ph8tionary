from django.shortcuts import render
from django.http import JsonResponse
from django.utils.safestring import mark_safe
import json


# Create your views here.
def hello_world(request):
    return JsonResponse({'foo': 'bar'})


# game/views.py
def index(request):
    return render(request, 'game/index.html', {})


def room(request, room_name):
    return render(request, 'game/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
