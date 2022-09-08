from tkinter.tix import Tree
from turtle import Turtle
from django.db import models

# Create your models here.

class AboutMe(models.Model):
    Ava="Available"
    Unv="Unvailable"
    Freelance = (
        (Ava, 'Available'),
        (Unv, 'Unvailable'),
      
    )
   
    name=models.CharField(max_length =80)
    designation=models.CharField(max_length=200)
    bio=models.CharField(max_length=230)
    about_me=models.TextField()
    degree = models.CharField(max_length=100)
    city = models.CharField(max_length=230)
    full_adders=models.CharField(max_length=150,blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    email = models.EmailField(verbose_name='email address', max_length=255,unique=True,)
    phone=models.IntegerField(blank=True,null=True)
    freelance = models.CharField(max_length=13, choices=Freelance,blank=True,null=True,default=Ava)


    profile_pictuer=models.ImageField(upload_to ='profile/')
    cover_picture=models.ImageField(upload_to ='coverpictue/')


    faceboock_link=models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    skype= models.URLField(blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    
    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.profile_pictuer.url))

    image_tag.short_description = 'ProfileImage'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["create_at"]
        verbose_name_plural = "AboutMe"

class Counts(models.Model):
    id = models.AutoField(primary_key=True)
    total_project = models.IntegerField(blank=True,null=True)
    hours_of_support =models.IntegerField(blank=True,null=True)
    awards = models.IntegerField(blank=True,null=True)
    happy_clients=models.IntegerField(blank=True,null=True)

    create_at = models.DateTimeField(auto_now_add=True,null=True)
    update_at = models.DateTimeField(auto_now=True,null=True)

    

    class Meta:
        ordering = ["create_at"]
        verbose_name_plural = "Counts"
    




class TESTIMONIALS(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length =80)
    designation=models.CharField(max_length=200)
    message=models.TextField()
    profile_pic=models.ImageField(upload_to ='testimonials/',blank=True,null=True)
    create = models.DateTimeField(auto_now_add=True, null=True)
    update= models.DateTimeField(auto_now=True,null=True)



    def __str__(self):
        return self.name

    class Meta:
        ordering = ["create"]
        verbose_name_plural = "Testimonials"


class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    Skill_name = models.CharField(blank=True, max_length=25)
    Skill_percentage= models.IntegerField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Skill_name

    class Meta:
        ordering = ["create_at"]
        verbose_name_plural = "Skills"




class Education(models.Model):
    id = models.AutoField(primary_key=True)
    lavel = models.CharField(max_length=150)
    campus_name = models.CharField(max_length=220)
    year = models.CharField(max_length=10)
    details = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lavel

class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=150)
    location = models.CharField(max_length=220)
    year = models.CharField(max_length=10)
    lavel_1 = models.CharField(max_length=250,blank=True,null=True)
    lavel_2 = models.CharField(max_length=250,blank=True,null=True)
    lavel_3 = models.CharField(max_length=250,blank=True,null=True)
    lavel_4 = models.CharField(max_length=250,blank=True,null=True)
    lavel_5 = models.CharField(max_length=250,blank=True,null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description



class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=300)
    sort_description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='service_img')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.logo.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

class Portfolio_Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, max_length=300)
    pro_category = models.ForeignKey(Portfolio_Category, on_delete=models.CASCADE)
    full_catefory_name=models.CharField(max_length=50,blank=True,null=True)
    Client_adderss=models.CharField(max_length=100,blank=True,null=True)
    project_url=models.URLField(blank=True,null=True)
    image = models.ImageField(upload_to='portfolio_img',blank=True)
    details =models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title
#extra image for portfolio 
class Extera_Images(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    eimage = models.ImageField(blank=True, upload_to='product_pic/')

    def __str__(self):
        return self.title 



class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=300,blank=True)
    meassage = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    update_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["create_at"]
        verbose_name_plural = "Contact"


    
    
