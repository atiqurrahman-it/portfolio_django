from webbrowser import get

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserContact
from .models import (TESTIMONIALS, AboutMe, Counts, Education, Experience,
                     Extera_Images, Portfolio, Portfolio_Category, Service,
                     Skills)

# Create your views here.

def HomePage(request):
    try:
        aboutMe = get_object_or_404(AboutMe)
    except:
        aboutMe = AboutMe.objects.last() # if two or more data in databse then last data find out 
    
    try:
        count = get_object_or_404(Counts)
    except:
        count = Counts.objects.last() # if two or more data in databse then last data find out 

    skill = Skills.objects.all().order_by('-id')[:6]
    testimonial=TESTIMONIALS .objects.all().order_by('-id')
    services=Service.objects.all().order_by('-id')[:6]
    educations=Education.objects.all().order_by('-id')[:3]
    experiences=Experience.objects.all().order_by('-id')[:2]
    portfolio_cat=Portfolio_Category.objects.all().order_by('-id')[:5]
    portfolio=Portfolio.objects.all().order_by('-id')

    # Contact part 
    if request.method == 'POST':
        form = UserContact(request.POST)
        if form.is_valid():
            form.save()
            #Counts.objects.create(name=name, email=email, subject=subject, meassage=message)

            #  email body for send me 
            from_email=form.cleaned_data.get("email")
            subject=form.cleaned_data.get("subject")
            name=form.cleaned_data.get('name')
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'details': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            # this mail send  message
            # to_email = settings.EMAIL_HOST_USER
            # send_mail(subject, message, from_email, [to_email])
            print(message)
            messages.success(request, name+' thanks for Contac')
            
            return redirect('/')
        else:
            print("form is error")
    else:
        form = UserContact()
    # End contact 


    data={
        "aboutme":aboutMe,
        "count":count,
        "skills":skill,
        "testimonials":testimonial,
        "services":services,
        "educations":educations,
        "experiences":experiences,
        "portfolio_cat":portfolio_cat,
        "portfolio":portfolio,
        "form":form,
    }
    return render(request,'index.html',data)



def PortfolioSingleView(request,prot_id):
    try:
        pro =get_object_or_404(Portfolio,id=prot_id)
        # extra image for portfolio
        extra_image=Extera_Images.objects.filter(id=pro.id)
    except:
        pass
    #optinal part for body bacground pictuer show er jonno
    try:
        aboutMe = get_object_or_404(AboutMe)
    except:
        aboutMe = AboutMe.objects.latest('id') 

    data={
        "portfoliodetails":pro,
        "extra_image":extra_image,
        "aboutme":aboutMe,
       
    }
    return render(request,'portfolio-details.html',data)




    