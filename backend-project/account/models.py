from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(_('نام'),max_length=100)
    last_name = models.CharField(_('نام خانوادگی'),max_length=100)
    image = models.ImageField(_('تصویر کاربر'),upload_to='profile_images/',default='static/images/profile.jpg')
    email = models.EmailField(_('ایمیل'),unique=True)
    phone = models.CharField(_('شماره تلفن'),max_length=15)
    address = models.TextField(_('آدرس'))
    zip_code = models.CharField(_('کد پستی'),max_length=20)
    is_active = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')

    def __str__(self):
        return self.username

    #def get_absolute_url(self):
    #    return reverse('account:profile', args=[self.id])