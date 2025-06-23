from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["title","status"]
    search_fields=["title"]
    list_filter=["status"]

@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=["name","price","status"]
    search_fields=["name"]
    list_filter=["status"]