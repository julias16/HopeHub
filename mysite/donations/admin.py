from django.contrib import admin
from .models import Item, Donation, Chat

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'donor', 'donor_phone', 'donor_address')
    search_fields = ('item_name', 'donor__username')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'category', 'donor', 'quantity', 'address', 'created_at')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'sender', 'message', 'timestamp')
