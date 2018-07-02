# django
from django.contrib import admin

# local
from .models import Category, Include, NoInclude, Recommendation

admin.site.register(Category)
admin.site.register(Include)
admin.site.register(NoInclude)
admin.site.register(Recommendation)
