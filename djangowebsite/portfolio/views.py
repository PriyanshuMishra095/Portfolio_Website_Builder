import random
import string
from django.shortcuts import render
from .models import About, Review, Event, PortfolioItem

from django.shortcuts import render, redirect
from .models import About, Review, Event, PortfolioItem
from .forms import AboutForm, ReviewForm, EventForm, PortfolioItemForm

# Create your views here.

def index(request,id):
    a = About.objects.get(id=id)
    r = Review.objects.filter(about_id=a.id)
    e = Event.objects.filter(about_id=a.id)
    p = PortfolioItem.objects.filter(about_id=a.id)
    context = {"data":
               {"name": a.name,
                "logo": a.logo,
                "icon": a.icon,
                "about": a.about,
                "work_title": a.work_title,
                "work_desc": a.work_desc,
                "experience_years": a.experience_years,
                "skill_1_title": a.skill_1_title,
                "skill_1_desc": a.skill_1_desc,
                "skill_2_title": a.skill_2_title,
                "skill_2_desc": a.skill_2_desc,
                "skill_3_title": a.skill_3_title,
                "skill_3_desc": a.skill_3_desc,
                "skill_4_title": a.skill_4_title,
                "skill_4_desc": a.skill_4_desc,
                "talent_1_title": a.talent_1_title,
                "talent_1_perc": a.talent_1_perc,
                "talent_2_title": a.talent_2_title,
                "talent_2_perc": a.talent_2_perc,
                "talent_3_title": a.talent_3_title,
                "talent_3_perc": a.talent_3_perc,
                "age": a.age,
                "insta_ID": a.insta_ID,
                "img":"img/slider-img.png",
                "reviews":r,
                "events":e,
                "portfolio":p

               }}
    return render(request, "index.html", context)

def form(request):

    form = AboutForm(prefix='aboutForm')
    portForm = PortfolioItemForm(prefix='portForm')
    reviewForm = ReviewForm(prefix='reviewForm')
    eventForm = EventForm(prefix='eventForm')

    context = {"data":{
            "img":"img/slider-img.png",'aboutForm': form,"portForm":portForm, 'reviewForm':reviewForm, 'eventForm':eventForm}}

    c = 0
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, prefix='aboutForm')
        id = ""
        key = string.ascii_letters + string.digits
        for x in range(1,5):
            id+=random.choice(key)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id = id
            obj.save()
            context['aboutForm'] = form
            c+=1

        portForm = PortfolioItemForm(request.POST, request.FILES, prefix='portForm')
        if portForm.is_valid():
            portFormObj = portForm.save(commit=False)
            portFormObj.about_id = obj.id
            portForm.save()
            context['portForm'] = portForm
            c+=1
        
        reviewForm = ReviewForm(request.POST, request.FILES,  prefix='reviewForm')
        if reviewForm.is_valid():
            reviewFormObj = reviewForm.save(commit=False)
            reviewFormObj.about_id = obj.id
            reviewForm.save()
            context['reviewForm'] = reviewForm
            c+=1
        
        eventForm = EventForm(request.POST, request.FILES, prefix='eventForm')
        if eventForm.is_valid():
            eventFormObj = eventForm.save(commit=False)
            eventFormObj.about_id = obj.id
            eventForm.save()
            context['eventForm'] = eventForm
            c+=1

        if c == 4:
            return redirect('index',id)
    
    return render(request, 'about.html', context)

