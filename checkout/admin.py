from django.contrib import admin

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                        'subtotal', 'total', 
                        'original_cart', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone', 'country',
              'post_code', 'city', 'address_1',
              'address_2', 'county', 'subtotal', 'total', 
              'original_cart', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'subtotal', 'total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
