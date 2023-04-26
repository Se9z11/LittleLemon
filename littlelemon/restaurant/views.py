from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .models import MenuItem, Booking
from .serializers import MenuSerializers, BookingSerializers
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

# Create your views here. 
class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializers

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializers

class BookingViewsSet(ModelViewSet):
    queryset  = Booking.objects.all()
    serializer_class = BookingSerializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
