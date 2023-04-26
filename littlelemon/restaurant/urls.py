from django.contrib import admin
from django.urls import path,include
from .views import MenuItemsView, SingleMenuItemView

urlpatterns = [
        path('menu/', MenuItemsView.as_view()),
        path('menu/<int:pk>', SingleMenuItemView.as_view()),
]

