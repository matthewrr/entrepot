from django.shortcuts import render
from .models import *

#move to class-based views

def find_item(request):
    context = {}
    return render(request, 'inventory/content.html', context)

def add_item(request):
    
    buildings = Building.objects.all()
    rooms = Room.objects.all()
    fixtures = Fixture.objects.all()
    containers = Container.objects.all()
    articles = Article.objects.all()
    
    context = { 
        'models': {
            'Buildings': buildings,
            'Rooms': rooms,
            'Fixtures': fixtures,
            'Containers': containers,
            'Articles': articles
    }}

    return render(request, 'inventory/content.html', context)