from django.contrib import admin
from django_cascading_dropdown_widget.widgets import DjangoCascadingDropdownWidget
from django_cascading_dropdown_widget.widgets import CascadingModelchoices
from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = []
        widgets = {
            "container": DjangoCascadingDropdownWidget(choices=CascadingModelchoices({
                "model": Container,
                "related_name": "containers",
            },
            )),
        }

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ["name", "quantity"]

admin.site.register(Building)
admin.site.register(Room)
admin.site.register(RoomSection)
admin.site.register(Fixture)
admin.site.register(ContainerTemplate)
admin.site.register(Container)
admin.site.register(Article, ArticleAdmin)
admin.site.register(QRCode)