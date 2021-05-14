from django.contrib import admin
from . models import Memory,Category,Tag
# Register your models here.

@admin.register(Memory)

class MemoryAdmin (admin.ModelAdmin):
    list_display=('name','date')

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}


@admin.register(Tag)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}