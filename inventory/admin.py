from django.contrib import admin
from .models import *

admin.site.register(Building)
admin.site.register(Room)
admin.site.register(RoomSection)
admin.site.register(Fixture)
admin.site.register(ContainerTemplate)
admin.site.register(Container)
admin.site.register(Article)
admin.site.register(QRCode)