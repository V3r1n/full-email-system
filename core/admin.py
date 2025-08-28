from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Queue, Ticket

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'name', 'phone_number', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'phone_number')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Queue)
admin.site.register(Ticket)
