from django.contrib.auth.models import User
from rest_framework import serializers

from search.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for Customers
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Customer
        fields = ['cust_id', 'cust_name', 'contact_num', 'created', 'owner']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for Users
    """
    customer = serializers.PrimaryKeyRelatedField(many=True, queryset=Customer.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'customer']
