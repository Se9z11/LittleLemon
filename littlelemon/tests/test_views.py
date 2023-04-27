from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializers

class MenuViewTest(TestCase):
    def setup(self):
        self.item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = MenuItem.objects.create(title="Chocolate", price=120, inventory=100)
        self.item3 = MenuItem.objects.create(title="Cake", price=60, inventory=100)

    def test_getall(self):
        response = self.client.get('/menus/')
        menus = MenuItem.objects.all()
        serializer = MenuSerializers(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)