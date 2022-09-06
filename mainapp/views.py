from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import AboutMe,Skills,TESTIMONIALS,Counts,Service,Education

from .forms import UserContact

# Create your views here.

def HomePage(request):
    
    try:
        aboutMe = get_object_or_404(AboutMe)
    except:
        aboutMe = AboutMe.objects.latest('id') # if two or more data in databse then last data find out 

    try:
        count = get_object_or_404(Counts)
    except:
        count = Counts.objects.latest('id') # if two or more data in databse then last data find out 

    skill = Skills.objects.all().order_by('-id')[:6]
    testimonial=TESTIMONIALS .objects.all().order_by('-id')
    services=Service.objects.all().order_by('-id')[:6]
    educations=Education.objects.all().order_by('-id')[:3]

    # Contact part 
    if request.method == 'POST':
        form = UserContact(request.POST)
        print(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            Message = form.cleaned_data.get('Message')
            print(name)
            print(email)
            print(subject)
            Counts.objects.create(name=name, email=email, subject=subject, Meassage=Message)
        else:
            print("error form ")
    else:
        contact=UserContact()


    data={
        "aboutme":aboutMe,
        "count":count,
        "skills":skill,
        "testimonials":testimonial,
        "services":services,
        "educations":educations,
        "form":contact,
    }



    return render(request,'mainapp/index.html',data)

def ContactPage(request):
   
    return render(request,'mainapp/about_me.html')
    