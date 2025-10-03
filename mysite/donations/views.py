from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Donation

from django.shortcuts import render, get_object_or_404
from .models import Item
@login_required
def donationform(request):
    if request.method == 'POST':
        donor = request.user
        item_name = request.POST.get('item_name')
        item_image = request.FILES.get('file_upload')
        category = request.POST.get('item_type')
        quantity = request.POST.get('quantity')
        donor_phone = request.POST.get('donor_phone')
        donor_address = request.POST.get('donor_address')

        Donation.objects.create(
            donor=donor,
            item_name=item_name,
            item_image=item_image,
            category=category,
            quantity=quantity,
            donor_phone=donor_phone,
            donor_address=donor_address,
        )

        # Show thank you message
        messages.success(request, f"Thank you for donating {category.capitalize()}!")

        # Redirect to corresponding receive page
        if category == 'food':
            return redirect('foodreceive')
        elif category == 'clothes':
            return redirect('clothsreceive')  # note spelling
        else:
            return redirect('furniturereceive')

    return render(request, 'donations/donateform.html')


# Receive pages
def foodreceive(request):
    items = Donation.objects.filter(category='food')
    return render(request, 'donations/foodreceive.html', {'items': items})


def clothsreceive(request):
    items = Donation.objects.filter(category='clothes')
    return render(request, 'donations/clothsreceive.html', {'items': items})


def furniturereceive(request):
    items = Donation.objects.filter(category='furniture')
    return render(request, 'donations/furniturereceive.html', {'items': items})


def item_detail(request, item_id):
    item = get_object_or_404(Donation, id=item_id)
    context = {
        'item': item,
        'donor': item.donor,
    }
    return render(request, 'donations/item_detail.html', context)



@login_required
def send_message(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        msg_text = request.POST.get('message')
        if msg_text:
            Chat.objects.create(item=item, sender=request.user, message=msg_text)
            messages.success(request, "Message sent!")
    return redirect('item_detail', item_id=item_id)

