from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['item_name', 'category', 'item_image', 'donor_phone', 'donor_address']
