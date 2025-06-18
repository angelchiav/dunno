from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Shipping)
admin.site.register(Product)

