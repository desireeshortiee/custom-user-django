from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, id_number, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not id_number:
            raise ValueError(_('The ID number field must be set'))

        email = self.normalize_email(email)
        user = self.model(id_number=id_number, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user