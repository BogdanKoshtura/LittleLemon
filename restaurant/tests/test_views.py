from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from ..models import Menu
from .. serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        
        Menu.objects.create(title="Burger", price=5.99, inventory=10)
        Menu.objects.create(title="Fries", price=2.99, inventory=50)
        Menu.objects.create(title="Coke", price=1.99, inventory=20)
        
    def test_detail(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)