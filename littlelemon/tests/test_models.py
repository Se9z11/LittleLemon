from django.test import TestCase

from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Beef Sandwich', price=80, inventory=100)
        self.assertEqual(item, MenuItem.objects.get(title='Beef Sandwich'))
