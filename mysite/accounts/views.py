from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import get_user_model

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']

            # Authenticate by username, email or phone
            user = authenticate(request, username=identifier, password=password)

            if user is None:
                # Try email
                User = get_user_model()
                try:
                    user_obj = User.objects.get(email=identifier)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass

                # Try phone
                try:
                    user_obj = User.objects.get(phone=identifier)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass

            if user is not None:
                login(request, user)

                # Check if user is admin
                if user.is_staff or user.is_superuser:
                    return redirect('admin:index')  # Django admin dashboard
                else:
                    return redirect('profile')  # Normal user profile page
            else:
                messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm

@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'accounts/profile.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def donate_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_or_phone = request.POST.get('email_or_phone')
        address = request.POST.get('address')
        item_type = request.POST.get('item_type')
        quantity = request.POST.get('quantity')
        item_details = request.POST.get('item_details')
        delivery_option = request.POST.get('delivery_option')
        file_upload = request.FILES.get('file_upload')

        # Save data logic here
        messages.success(request, "Thank you! Your donation request has been received.")
        return redirect('donateform')

    return render(request, 'accounts/donation_form.html')

