from django.shortcuts import render
from rest_framework import viewsets

from apps.customers.models import Customer
from apps.customers.serializers import CustomerSerializer


def index(request):
    return render(request, 'customers/index.html')


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited
    """
    queryset = Customer.objects.all().order_by('-first_name', '-last_name')
    serializer_class = CustomerSerializer
