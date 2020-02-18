"""
URL Patterns
"""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from search.views import CustomerViewSet, UserViewSet, api_root, SearchViewSet


CUSTOMER_LIST = CustomerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

CUSTOMER_DETAIL = CustomerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

CUSTOMER_SEARCH = SearchViewSet.as_view({
    'get': 'retrieve'
})

USER_LIST = UserViewSet.as_view({
    'get': 'list'
})

USER_DETAIL = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('customer/', CUSTOMER_LIST, name='customer-list'),
    path('customer/<int:pk>/', CUSTOMER_DETAIL, name='customer-detail'),
    path('search/<int:contact>/', CUSTOMER_SEARCH, name='customer-search'),
    path('users/', USER_LIST, name='user-list'),
    path('users/<int:pk>/', USER_DETAIL, name='user-detail'),
    path('', api_root),
])
