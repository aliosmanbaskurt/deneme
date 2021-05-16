from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('index/',views.index, name="index"),
    path('future/',views.future, name="future"),
    path('story/',views.story, name="story"),
   



       
]