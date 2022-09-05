from django.contrib import admin
from .models import AboutMe

# Register your models here.

class AboutMe_admin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'email', 'update_at']

    class Meta:
        Model = AboutMe


admin.site.register(AboutMe, AboutMe_admin)
