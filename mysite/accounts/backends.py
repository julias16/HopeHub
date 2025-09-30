from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q  # <- এটা import করতে হবে

User = get_user_model()

class CustomBackend(ModelBackend):
    """
    Allows authentication with username, email, or phone.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('identifier')
        try:
            user = User.objects.get(
                Q(username__iexact=username) |
                Q(email__iexact=username) |
                Q(phone__iexact=username)
            )
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
