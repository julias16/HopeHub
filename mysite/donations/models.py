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
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} ({self.category}) by {self.donor.username}"
