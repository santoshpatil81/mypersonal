from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .models import Customer
from .serializers import CustomerSerializer
from .views import CustomerViewSet, SearchViewSet


class CustomerTests(APITestCase):
    """"
    Test CustomerViewSet and SearchViewSet
    """

    def setUp(self):
        self.username = "test"
        self.email = "test@test.com"
        self.password = "testing customer"
        self.user = User.objects.create_user(
            self.username, self.email, self.password
        )
        user = User.objects.get(username='test')

        Customer.objects.create(
            cust_name='John', contact_num='12345678999', owner=user)

    # create customer
    def test_create_customer(self):
        request = APIRequestFactory().get("")
        cust_detail = CustomerViewSet.as_view({'get': 'retrieve'})
        cust = Customer.objects.create(cust_name="John")
        response = cust_detail(request, pk=cust.pk)
        self.assertEqual(response.status_code, 200)

    # get customer details
    def test_get_customer_cust_name(self):
        request = APIRequestFactory().get("")
        cust_detail = CustomerViewSet.as_view({'get': 'retrieve'})
        response = cust_detail(request, pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().cust_name, "John")

    # get customer based on contact number
    def test_get_customer_contact_num(self):
        request = APIRequestFactory().get("")
        cust_detail = SearchViewSet.as_view({'get': 'retrieve'})
        response = cust_detail(request, contact="12345678999")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().cust_name, "John")


class TestCustomerModel(TestCase):
    """
    Test Customer model
    """

    def setUp(self):
        self.username = "test"
        self.email = "test@test.com"
        self.password = "testing customer"
        self.user = User.objects.create_user(
            self.username, self.email, self.password
        )
        user = User.objects.get(username='test')

        Customer.objects.create(
            cust_name='John', contact_num='12345678999', owner=user)
        Customer.objects.create(
            cust_name='Milo', contact_num='12345678888', owner=user)

    # get customer name based on contact number
    def test_cust_name(self):
        cust_john = Customer.objects.get(contact_num='12345678999')
        cust_milo = Customer.objects.get(contact_num='12345678888')
        self.assertEqual(
            cust_john.get_cust_name(), "John")
        self.assertEqual(
            cust_milo.get_cust_name(), "Milo")

    # get customer based on name
    def test_contact_num(self):
        cust_john = Customer.objects.get(cust_name='John')
        cust_milo = Customer.objects.get(cust_name='Milo')
        self.assertEqual(
            cust_john.get_contact_num(), '12345678999')
        self.assertEqual(
            cust_milo.get_contact_num(), '12345678888')


class TestCustomerSerializer(TestCase):
    """
    Test Customer Serializer
    """

    def setUp(self):
        self.username = "test"
        self.email = "test@test.com"
        self.password = "testing customer"
        self.user = User.objects.create_user(
            self.username, self.email, self.password
        )
        user = User.objects.get(username='test')

        self.cust_attributes = {
            'cust_name': 'Andrew',
            'contact_num': '1234567777'
        }

        self.serializer_data = {
            'cust_id': 100,
            'cust_name': 'Joe',
            'contact_num': '12345666666',
            'owner': 'test',
            'created': datetime.now()
        }

        self.cust = Customer.objects.create(**self.cust_attributes)
        self.serializer = CustomerSerializer(instance=self.cust)

    # test serializer returns all fields
    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['cust_name', 'contact_num', 'owner', 'created', 'cust_id']))

    # test serializer returns valid cust_name
    def test_name_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['cust_name'], self.cust_attributes['cust_name'])

    # test serializer returns valid contact number
    def test_contact_num_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['contact_num'], self.cust_attributes['contact_num'])
        self.assertNotEqual(data['contact_num'], self.serializer_data['contact_num'])

    # test created customer is valid
    def test_serializer_data_saves_in_db(self):
        serializer = CustomerSerializer(data=self.serializer_data)
        serializer.is_valid()
        new_cust = serializer.save()
        new_cust.refresh_from_db()

        self.assertEqual(new_cust.cust_name, 'Joe')
        self.assertEqual(new_cust.contact_num, '12345666666')
        self.assertNotEqual(new_cust.cust_id, '100')

    # test searching customer based on contact number
    def test_matching_contact_num(self):
        serializer = CustomerSerializer(data=self.serializer_data)
        serializer.is_valid()
        new_cust = serializer.save()
        new_cust.refresh_from_db()

        self.assertEqual(new_cust.cust_name, 'Joe')
        self.assertIn('666666', new_cust.contact_num)
        self.assertNotIn('7', new_cust.contact_num)
