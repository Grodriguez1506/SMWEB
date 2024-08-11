from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser, Company, WorkOrder, FinishedOrder, DeletedOrder, InvoicedOrder, OrderPayment, Worker

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'company__name')
    list_display = ('first_name', 'last_name','company', 'rol')

class WorkOrderAdmin(admin.ModelAdmin):
    search_fields = ('order_id', 'client', 'city', 'service_description', 'in_charge')
    list_display = ('order_id', 'in_charge','client', 'city', 'status', 'sales_value')
    readonly_fields = ('created_at',)

class FinishedOrderAdmin(admin.ModelAdmin):
    search_fields = ('order_id', 'client', 'city', 'service_description', 'in_charge')
    list_display = ('order_id', 'in_charge','client', 'city', 'status', 'sales_value', 'finished_at')
    readonly_fields = ('finished_at',)

class InvoicedOrderAdmin(admin.ModelAdmin):
    search_fields = ('order_id', 'client', 'city', 'service_description', 'in_charge')
    list_display = ('order_id', 'in_charge','client', 'city', 'status', 'sales_value', 'invoiced_at')
    readonly_fields = ('invoiced_at',)

class DeletedOrderAdmin(admin.ModelAdmin):
    search_fields = ('order_id', 'client', 'city', 'service_description', 'in_charge')
    list_display = ('order_id', 'in_charge','client', 'city', 'status', 'sales_value', 'deleted_at')
    readonly_fields = ('deleted_at',)

class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'status','users_limit', 'created_at')
    readonly_fields = ('created_at',)

class OrderPaymentAdmin(admin.ModelAdmin):
    search_fields = ('order_id', 'client', 'city', 'made_by', 'in_charge')
    list_display = ('order_id', 'in_charge','client', 'city', 'amount')
    readonly_fields = ('created_at',)

admin.site.unregister(Group)

admin.site.register(FinishedOrder, FinishedOrderAdmin)
admin.site.register(DeletedOrder, DeletedOrderAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(InvoicedOrder, InvoicedOrderAdmin)
admin.site.register(OrderPayment, OrderPaymentAdmin)
admin.site.register(Worker)


