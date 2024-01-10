from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search_for_items/",views.search_for_items, name="search_for_items"),
    path("newPage/",views.newPage, name="newPage"), 
    path("edit/",views.edit, name="edit"), 
    path("saveEdit/",views.saveEdit, name="saveEdit"),
    path("randomPage/",views.randomPage, name="randomPage") 
    
]
