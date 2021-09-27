from django.contrib import admin
from django.db import models
from django.db.models import fields
from .models import Product, Orderitem,Order
@admin.register(Product)
class Myproduct(admin.ModelAdmin):
    
    list_display=["category", "p_name", "price"]

class Orderiteminline(admin.TabularInline):
    model=Orderitem
    raw_id_fields=['product']
@admin.register(Order)
class Myorder(admin.ModelAdmin):
    
    list_display=["name", "email", "contact"]
    inlines=[Orderiteminline]

# Register your models here.
