from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Donation



@login_required
def donationform(request):
    if request.method == 'POST':
        donor = request.user
        category = request.POST.get('item_type')  # template name = item_type
        item_name = request.POST.get('item_details')  # template er textarea
        item_image = request.FILES.get('file_upload')
        quantity = request.POST.get('quantity')
        address = request.POST.get('address')

        # Create donation
        Donation.objects.create(
            donor=donor,
            category=category,
            item_name=item_name,
            item_image=item_image,
            quantity=quantity,
            address=address,
            details=item_name,  # same as item_name here
            delivery_option='Self'  # optional
        )

        # Show thank you message
        messages.success(request, f"Thank you for donating {category.capitalize()}!")

        # Redirect to corresponding receive page
        if category == 'food':
            return redirect('foodreceive')
        elif category == 'clothes':
            return redirect('clothesreceive')
        else:
            return redirect('furniturereceive')

    return render(request, 'donationform.html')


# Receive pages
def foodreceive(request):
    items = Donation.objects.filter(category='food')
    return render(request, 'foodreceive.html', {'items': items})


def clothesreceive(request):
    items = Donation.objects.filter(category='clothes')
    return render(request, 'clothsreceive.html', {'items': items})


def furniturereceive(request):
    items = Donation.objects.filter(category='furniture')
    return render(request, 'furniturereceive.html', {'items': items})
