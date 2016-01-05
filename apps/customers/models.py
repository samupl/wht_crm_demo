from django.db import models


class Customer(models.Model):
    HARDWARE_TYPES = {
        1: 'Car',
        2: 'Motorcycle',
        3: 'Bus'
    }
    first_name = models.CharField('First name', max_length=256)
    last_name = models.CharField('Last name', max_length=256)
    address = models.CharField('Address', max_length=512)
    hardware_type = models.IntegerField('Hardware type', choices=list(HARDWARE_TYPES.items()))
    review_date = models.DateField('Review date')
    comments = models.CharField('Comments', max_length=1024, null=True, blank=True)
