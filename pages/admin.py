from django.contrib import admin
from . models import Future

# Register your models here.

@admin.register(Future)

class FutureAdmin (admin.ModelAdmin):
    list_display=('future_name',)