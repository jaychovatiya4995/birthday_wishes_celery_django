from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BirthdayWishes

class birthday_wishes_admin(UserAdmin):   
    list_display = ('username', 'email','birthdate')
    
    fieldsets = (
        (None, {
            'fields' : ('username', 'email','birthdate')
        })
    )
    
    add_fieldsets = (
        (None, {
            'fields' : ('username', 'email','birthdate')
        })
    )
    
admin.site.register(BirthdayWishes)
