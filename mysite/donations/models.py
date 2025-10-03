from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Donation(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('clothes', 'Clothes'),
        ('furniture', 'Furniture'),
    ]

    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    item_name = models.CharField(max_length=100)
    item_image = models.ImageField(upload_to='donation_images/')
    quantity = models.PositiveIntegerField()
    address = models.TextField()
    donor_phone = models.CharField(max_length=20, blank=True, null=True)
    donor_address = models.TextField(blank=True, null=True)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} ({self.category}) by {self.donor.username}"

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_image = models.ImageField(upload_to='items/')
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    donor_phone = models.CharField(max_length=20)
    donor_address = models.TextField()

    def __str__(self):
        return self.item_name

# Optional: Chat model
class Chat(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='chats')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.message[:20]}"