from urllib import request

from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(Customer)
admin.site.register(PaymentInfo)
admin.site.register(DeliveryAddress)
admin.site.register(Order)

# def __init__(self, myView):
    # MyView(request)