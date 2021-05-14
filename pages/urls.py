from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('future/',views.future, name="future"),
    path('story/',views.story, name="story"),
   



       
]