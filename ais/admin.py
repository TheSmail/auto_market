from django.contrib import admin
from .models import *

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    # raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    # list_display = ['id', 'status', 'date_create', 'date_end']
    # list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Contractor)