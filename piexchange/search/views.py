
"""
"""

from django.contrib.auth.models import User
from rest_framework import viewsets, renderers, reverse
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from search.models import Customer
from search.serializers import CustomerSerializer, UserSerializer
from . import permissions
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request):
    """
    API root
    """
    return Response({'users': reverse('user-list', request=request, format=format),
                     'customer': reverse('customer-list', request=request, format=format)})


class CustomerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Customers.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        """
        Create customer object
        """
        serializer.save(owner=self.request.user)


class SearchViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides search actions
    for Customers based on patterns of their contact numbers.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def retrieve(self, serializer, contact):
        """
        Retrieve customers
        """
        customers = Customer.objects.all()
        if contact is not None:
            customers = customers.filter(contact_num__contains=contact)
            serializer = CustomerSerializer(customers, many=True)

        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
