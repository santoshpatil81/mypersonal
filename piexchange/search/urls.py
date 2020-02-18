from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from search.views import CustomerViewSet, UserViewSet, api_root, SearchViewSet

customer_list = CustomerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

customer_detail = CustomerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

customer_search = SearchViewSet.as_view({
    'get': 'retrieve'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('customer/', customer_list, name='customer-list'),
    path('customer/<int:pk>/', customer_detail, name='customer-detail'),
    path('search/<int:contact>/', customer_search, name='customer-search'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('', api_root),
])
