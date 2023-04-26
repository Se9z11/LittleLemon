from django.contrib import admin
from django.urls import path,include
from .views import MenuItemsView, SingleMenuItemView
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
        path('menu/', MenuItemsView.as_view()),
        path('menu/<int:pk>', SingleMenuItemView.as_view()),
        path('message/', views.msg),
        path('api-token-auth/', obtain_auth_token),
]

