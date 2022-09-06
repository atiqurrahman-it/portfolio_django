from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import AboutMe,Skills,TESTIMONIALS,Counts,Service,Education,Experience
from django.http import HttpResponseRedirect

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
    experiences=Experience.objects.all().order_by('-id')[:2]

    # Contact part 
    if request.method == 'POST':
        print(request.post)
        form = UserContact(request.POST)
        if form.is_valid():
            Message = form.cleaned_data.get('Message')
            print(Message)
            #Counts.objects.create(name=name, email=email, subject=subject, Meassage=Message)
            return HttpResponseRedirect('/thanks/')
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
        "form":form,
    }
    return render(request,'index.html',data)




    