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
        category = request.POST.get('item_type')  # template input name
        item_name = request.POST.get('item_name')
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
    item = get_object_or_404(Item, id=item_id)
    chats = item.chats.all().order_by('timestamp')  # chat history
    context = {
        'item': item,
        'donor': item.donor,
        'chats': chats,
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

