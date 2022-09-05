from django.contrib import admin
from .models import AboutMe,Skills,TESTIMONIALS,Counts

# Register your models here.

class AboutMe_admin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'email', 'update_at']

    class Meta:
        Model = AboutMe
admin.site.register(AboutMe, AboutMe_admin)


class Skills_admin(admin.ModelAdmin):
    list_display = ['Skill_name', 'Skill_percentage', 'update_at']

    class Meta:
        Model = Skills
admin.site.register(Skills, Skills_admin)


class TESTIMONIALS_admin(admin.ModelAdmin):
    list_display = ['name', 'designation','create',]

    class Meta:
        Model = TESTIMONIALS
admin.site.register(TESTIMONIALS, TESTIMONIALS_admin)


class Counts_admin(admin.ModelAdmin):
    list_display = ['total_project', 'awards','create_at',]

    class Meta:
        Model = Counts
admin.site.register(Counts, Counts_admin)


