from rest_framework.serializers import ModelSerializer
from .models import MenuItem, Booking
from django.contrib.auth.models import User

class MenuSerializers(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

class BookingSerializers(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']