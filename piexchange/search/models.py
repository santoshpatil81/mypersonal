from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    """
    Schema for Customer model
    """
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=254, null=False)
    contact_num = models.TextField(max_length=11)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='customer', on_delete=models.CASCADE, default='1')

    def get_cust_name(self):
        return self.cust_name

    def get_contact_num(self):
        return self.contact_num

    class Meta:
        ordering = ['created', 'contact_num']


def save(self, *args, **kwargs):
    """

    :type args: Customer
    """
    super(self, Customer).save(*args, **kwargs)
