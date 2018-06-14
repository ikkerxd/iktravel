# django
from django.contrib import admin

# local
from .models import Category, Include, NoInclude, Country


admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Include)
admin.site.register(NoInclude)
