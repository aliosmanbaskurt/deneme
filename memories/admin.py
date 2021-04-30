from django.contrib import admin
from . models import Memory,Category
# Register your models here.

@admin.register(Memory)

class MemoryAdmin (admin.ModelAdmin):
    list_display=('name','date')

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}