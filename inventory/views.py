from django.http import JsonResponse
from django.shortcuts import render
import qrcode

from .models import *
from .forms import ArticleForm

#move to class-based views
def view_items(request):
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

def add_item(request):
    form = ArticleForm()
    containers = Container.objects.all()
    rooms = Room.objects.all()
    fixtures = Fixture.objects.all()
    buildings = Building.objects.all()
    context = {
        'form': form,
        'categories': {
            'container': containers,
            'fixture': fixtures,
            'room': rooms,
            'building': buildings
        }
    }
    return render(request, 'inventory/item_add.html', context)
    
def item_categories(request):
    d = {}
    models = {'container': Container, 'room': Room, 'fixture': Fixture, 'building': Building}
    category = request.GET.get('category', None)
    model_name = models[category]
    try:
        objs = model_name.objects.values_list('name', flat=True)
    except:
        return JsonResponse(d)
    for i in range(len(objs)):
        d[i] = objs[i]
    #caching for reselection?
    #logic + frontend if category does not exist
    return JsonResponse(d)

def create_qr(data):
    img = qrcode.make(data)
    file_name = 'MyQRCode2.png'
    img.save(file_name)
    return

# CRUD
# +add item item_add ***VIEW**
# +read items/FILTER item_view_all ***VIEW**
# +read detail item_view_detail ***VIEW**
# +update item (?? --> under detail view) 
# +delete item (?? --> undre detail view)
#(search) (?? --> limit to search bar... mayybe view as well?... probably because filter w/o keyword) ***VIEW**