# from django.contrib import admin
# from .models import Train, Ticket
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Train, Ticket


# Register your models here.


# admin.site.register(Train)
# admin.site.register(Ticket)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # You can customize the admin interface for your custom user model here

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Train)
admin.site.register(Ticket)