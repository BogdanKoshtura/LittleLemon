from ..models import Menu, Booking
from django.test import TestCase

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=10)
        self.assertEqual(item.title, "IceCream")
        
class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="Jimmy", no_of_guests=8, booking_date= "2023-04-17 15:00")
        self.assertEqual(item.name, "Jimmy")
        