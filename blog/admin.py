from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    # Customize how Blog model is displayed in the Django Admin
    list_display = ('name', 'description', 'created_at', 'updated_at')

# Register the Blog model with the BlogAdmin class
admin.site.register(Blog, BlogAdmin)
