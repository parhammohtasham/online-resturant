from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_per_page = 10
    list_display_links = ('username', 'email')

    list_editable = ('is_active',)
   
    fieldsets =(
        (None , {"fields": ("username" , "first_name" , "last_name")}),
        ("اطلاعات تماس" , {"fields": ("email" , "phone" , "address" , "zip_code" )}),
        ("اطلاعات کاربر" , {"fields": ("is_active" , "image")}),
    )
    add_fieldsets = (
        (None , {"fields": ("username" , "first_name" , "last_name" , "password1" , "password2")}),
        ("اطلاعات تماس" , {"fields": ("email" , "phone" , "address" , "zip_code" )}),
        ("اطلاعات کاربر" , {"fields": ("is_active" ,  "image")}),
    )

