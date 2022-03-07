from django.shortcuts import render
# from .models import ClassName

def find_item(request):
    context = {}
    return render(request, 'inventory/base.html', context)