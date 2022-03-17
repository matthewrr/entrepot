from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView, UpdateView, 
    DetailView, DeleteView
)
from .models import *

class ItemListView(ListView):
    model = Article
    template_name = "inventory/item/item_list.html"
    context_object_name = "items"
class ItemDetailView(DetailView):
    model = Article
    template_name = "inventory/item/item_detail.html"
    context_object_name = "item"
class ItemUpdateView(UpdateView):
    model = Article
    fields = ('name','quantity','description',)
    template_name = "inventory/item/item_update.html"
class ItemDeleteView(DeleteView):
    model = Article
    template_name = "inventory/item/item_delete.html"
    success_url = reverse_lazy('item_list')
class ItemCreateView(CreateView):
    model = Article
    extra_context= {'container_type': ['container','fixture','room','building']}
    fields = ('name','quantity','description', 'img', 'tags', 'category', 'subcategory', 'content_type', 'high_value',)
    template_name = "inventory/item/item_create.html"
    success_url = reverse_lazy('item_list')

class ContainerListView(ListView):
    model = Container
    template_name = "inventory/container_list.html"
    context_object_name = "containers"
class ContainerDetailView(DetailView):
    model = Container
    template_name = "inventory/container_detail.html"
    context_object_name = "container"
class ContainerUpdateView(UpdateView):
    model = Container
    fields = ('name',)
    template_name = "inventory/caontiner_update.html"
class ContainerDeleteView(DeleteView):
    model = Container
    template_name = "inventory/container_delete.html"
    success_url = reverse_lazy('container_list')
class ContainerCreateView(CreateView):
    model = Container
    extra_context= {'container_type': ['container','fixture','room','building']}
    fields = ('name',)
    template_name = "inventory/container_create.html"
    success_url = reverse_lazy('container_list')

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
    return JsonResponse(d)

# import qrcode
# def create_qr(data):
#     img = qrcode.make(data)
#     file_name = 'MyQRCode2.png'
#     img.save(file_name)
#     return