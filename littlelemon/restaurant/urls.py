from django.contrib import admin
from django.urls import path,include
from .views import MenuItemsView, SingleMenuItemView
from restaurant import views

urlpatterns = [
        path('menu/', MenuItemsView.as_view()),
        path('menu/<int:pk>', SingleMenuItemView.as_view()),
        path('message/', views.msg),
]

