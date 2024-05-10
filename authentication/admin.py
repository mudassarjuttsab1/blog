from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    # Customize how User model is displayed in the Django Admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')

# Register the User model with the UserAdmin class
admin.site.register(User, UserAdmin)
