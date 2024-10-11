from django.contrib import admin

from web.models import Category, Tag, Blog


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)

