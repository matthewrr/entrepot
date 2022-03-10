from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Building(models.Model):
    name = models.CharField(max_length=100)
    default = models.BooleanField(default=False)
    #only populate address fields if requested by user
    address_1 = models.CharField(verbose_name='Street Address 1', max_length=100, blank=True)
    address_2 = models.CharField(verbose_name='Street Address 2', max_length=100, blank=True)
    address_city = models.CharField(verbose_name='City', max_length=100, blank=True)
    address_state = models.CharField(verbose_name="State", max_length=100, blank=True)
    address_zip = models.CharField(verbose_name='ZIP Code', max_length=100, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)
    default = models.BooleanField(default=False)
    floor = models.CharField(max_length=100, blank=True)
    room_number = models.CharField(max_length=100, blank=True) #choose more ambiguous attribute name?
    blueprint = models.ImageField(upload_to = "images/", blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        #only include if exists
        #create different function for combinations (def pwd(self)...)
        return f'{self.name}, Room Number: {self.room_number}, Floor: {self.floor}'

class RoomSection(models.Model):
    name = models.CharField(max_length=100, blank=True) #e.g. A1
    default = models.BooleanField(default=False)
    description = models.CharField(max_length=100, blank=True) #e.g. NE Wall
    map_color = models.CharField(max_length=6, blank=True) #use a color picker. optional and/or default options
    created_date = models.DateTimeField(default=timezone.now)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #way to overlay on map? ooh, see contents by shelf or section, etc.

    def __str__(self):
        return self.name

class Fixture(models.Model):
    category = models.CharField(max_length=100, blank=True) #allow previous entries as options, or popular choices
    default = models.BooleanField(default=False)
    description = models.CharField(max_length=100, blank=True) #hints like metal, color
    created_date = models.DateTimeField(default=timezone.now)
    room_section = models.ForeignKey(RoomSection, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.category

class ContainerAttributes(models.Model):
    name = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    material = models.CharField(max_length=100, blank=True)
    default_img = models.ImageField(upload_to = "images/", blank=True, null=True)
    user_img = models.ImageField(upload_to = "images/", blank=True, null=True)

    class Meta:
        abstract = True
    
class ContainerTemplate(ContainerAttributes):
    name = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(default=timezone.now) #make so can't inherit

class Container(ContainerAttributes):
    name = models.CharField(max_length=100, blank=True) #appears on label
    tags = TaggableManager(blank=True)
    notes = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    has_qr_code = models.BooleanField(default=False) #rename
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    # def save_container(self):
    #     pass

class Item(models.Model):
    name = models.CharField(max_length=100)
    quanity = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(blank=True) #set length (of all text fields)
    img = models.ImageField(upload_to = "images/", blank=True, null=True) #write as plural?
    high_value = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    category = models.CharField(max_length=100, blank=True) #should these be own class? multiselect
    subcategory = models.CharField(max_length=100, blank=True) #should these be own class? multiselect, cascading
    created_date = models.DateTimeField(default=timezone.now)
    #option for quick-add as list? utilize django-taggit for this?
    has_container = models.BooleanField(default=True) #rename?
    container = models.ForeignKey(Container, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class QRCode(models.Model):
    img = models.ImageField(upload_to = "images/", blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    container = models.OneToOneField(
        Container,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    #add option for container or item FK

class HighValue(models.Model):
    upc = models.CharField(max_length=100, blank=True)
    serial_number = models.CharField(max_length=100, blank=True)
    value = models.DecimalField(max_digits=9, decimal_places=2) #make optional?
    purchase_date = models.DateField(blank=True, null=True)
    img = models.ImageField(upload_to = "images/", blank=True, null=True) #upc/serial images? 2 img fields?
    created_date = models.DateTimeField(default=timezone.now)
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE, #only allow deletion when item.high_value marked false
        primary_key=True,
    )

    # def __str__(self):
    #     return self.upc