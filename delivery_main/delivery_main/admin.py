from django.contrib import admin
from .models import Customer, Category, Item, Order
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'email', 'phone_number']
  search_fields = ['first_name', 'last_name', 'email']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'description']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  list_display = ['item_name', 'customer', 'category', 'price', 'weight']
  list_filter = ['category']
  search_fields = ['item_name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ['customer', 'status', 'created_at', 'delivery_address']
  list_filter = ['status', 'created_at']
  search_fields = ['customer__first_name', 'customer__last_name']