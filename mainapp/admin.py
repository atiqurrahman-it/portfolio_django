from django.contrib import admin

from .models import (TESTIMONIALS, AboutMe, Contact, Counts, Education,
                     Experience, Extera_Images, Portfolio, Portfolio_Category,
                     Service, Skills)

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


class Service_admin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'create_at', 'update_at']
    search_fields = ["title", 'create_at']
    list_filter = ['create_at']

    class Meta:
        Model = Service
admin.site.register(Service, Service_admin)


class Education_admin(admin.ModelAdmin):
    list_display = ['lavel', 'year', 'create_at', 'update_at']
    search_fields = ["lavel", 'year']
    list_filter = ['create_at', 'lavel']

    class Meta:
        Model = Education
admin.site.register(Education, Education_admin)


class Experience_admin(admin.ModelAdmin):
    list_display = ['description', 'create_at', 'update_at']
    search_fields = ["description", 'year']
    list_filter = ['create_at', 'description']

    class Meta:
        Model = Experience
admin.site.register(Experience, Experience_admin)



class Portfolio_Category_admin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'update_at']
    search_fields = ["name", 'create_at']
    list_filter = ['create_at']

    class Meta:
        Model = Portfolio_Category

admin.site.register(Portfolio_Category, Portfolio_Category_admin)

#extra image for portfolio 
class PortfolioImagesInline(admin.TabularInline):
    model = Extera_Images
    extra = 1

class Portfolio_admin(admin.ModelAdmin):
    list_display = ['title', 'pro_category', 'image_tag', 'create_at', 'update_at']
    search_fields = ["title", 'create_at']
    list_filter = ['create_at']
    # extra image 
    inlines = [ PortfolioImagesInline]

    class Meta:
        Model = Portfolio
admin.site.register(Portfolio, Portfolio_admin)



class Contact_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_at', 'update_at']
    search_fields = ["name", 'email']
    list_filter = ['create_at', 'name', 'email']

    class Meta:
        Model = Contact


admin.site.register(Contact, Contact_admin)


