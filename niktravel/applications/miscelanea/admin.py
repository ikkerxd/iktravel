# django
from django.contrib import admin

# local
from .models import Category, Include, NoInclude

admin.site.register(Category)
admin.site.register(Include)
admin.site.register(NoInclude)
