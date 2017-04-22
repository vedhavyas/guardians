from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = [
        'id',
        'username',
        'password',
        'last_login',
    ]
