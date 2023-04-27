from django.test import TestCase

from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializers

class MenuViewTest(TestCase):

    def setUp(self):
        menu_item = MenuItem.objects.create(title='Beef Sandwich', price=12.90, inventory=100)
        menu_item = MenuItem.objects.create(title='Chicken Sandwich', price=10.90, inventory=50)


    def test_getall(self):
        url = 'http://127.0.0.1:8000/restaurant/menu/'
        
        response = self.client.get(url)

        menu_items = MenuItem.objects.all()
        serialized_menu_items = MenuSerializers(menu_items, many=True)

        self.assertEqual(response.data, serialized_menu_items.data)
