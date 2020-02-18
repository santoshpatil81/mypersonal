"""
Customer model
"""
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    Schema for Customer model
    """
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=254, null=False)
    contact_num = models.TextField(max_length=11)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        related_name='customer',
        on_delete=models.CASCADE,
        default='1')

    def get_customer_name(self):
        """
        :return: args: Customer
        """
        return self.cust_name

    def get_customer_contact_number(self):
        """
        :return: args: Customer
        """
        return self.contact_num

    class Meta:
        ordering = ['created', 'contact_num']
