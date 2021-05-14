from django.contrib import admin
from django.urls import path
from memories.views import MemoriesDetailView
from . import views


urlpatterns = [
    path('',views.memo_list, name="memories"),
    path('<slug:category_slug>/<int:memo_id>', MemoriesDetailView.as_view(), name="memory_detail"),
    path('categories/<slug:category_slug>', views.category_detail, name ="memories_by_category"),
    path('tag/<slug:tag_slug>', views.tag_list, name ="memories_by_tag"),   
    path('search/', views.search, name="search"),
]