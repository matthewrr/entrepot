from django.shortcuts import render
from .models import *
import qrcode

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

    data = buildings
    qr_code = create_qr(data)

    return render(request, 'inventory/content.html', context)

def create_qr(data):
    img = qrcode.make(data)
    file_name = 'MyQRCode2.png'
    img.save(file_name)
    return