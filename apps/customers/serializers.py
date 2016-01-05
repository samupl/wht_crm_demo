from rest_framework import serializers

from apps.customers.models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'address', 'hardware_type', 'review_date', 'comments')
