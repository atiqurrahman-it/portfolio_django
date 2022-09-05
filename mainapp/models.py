from django.db import models

# Create your models here.

class AboutMe(models.Model):
    name=models.CharField(max_length =80)
    designation=models.CharField(max_length=200)
    bio=models.CharField(max_length=230)
    about_me=models.TextField()
    degree = models.TextField(max_length=600)
    city = models.TextField(max_length=600)
    birthday = models.DateField(blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    email = models.EmailField(verbose_name='email address', max_length=255,unique=True,)
    phone=models.IntegerField(blank=True,null=True)

    profile_pictuer=models.ImageField(upload_to ='profile/')
    cover_picture=models.ImageField(upload_to ='coverpictue/')


    faceboock_link=models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    
    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.profile_pictuer.url))

    image_tag.short_description = 'ProfileImage'

    def __str__(self):
        return self.name


class TESTIMONIALS(models.Model):
    name=models.CharField(max_length =80)
    designation=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.name


class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    Skill_name = models.CharField(blank=True, max_length=25)
    Skill_percentage= models.IntegerField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Skill_name


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    Meassage = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
    
