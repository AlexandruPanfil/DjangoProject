from django.contrib import admin
from .models import *
# Register your models here.


class PCAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_update", "photo", "is_published")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


admin.site.register(PC, PCAdmin)
admin.site.register(Category, CategoryAdmin)
