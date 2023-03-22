from django.shortcuts import render
from .models import About, Review, Event, PortfolioItem
# Create your views here.


def index(request):
    a = About.objects.all()[0]
    r = Review.objects.filter(about_id=a.about_id)
    e = Event.objects.filter(about_id=a.about_id)
    context = {"data":
               {"name": a.name,
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
               }}
    return render(request, "index.html", context)

from django.shortcuts import render, redirect
from .models import About, Review, Event, PortfolioItem
from .forms import AboutForm, ReviewForm, EventForm, PortfolioItemForm

def about(request):
    if request.method == 'POST':
        print(request.POST)
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        portForm = PortfolioItemForm(request.POST, request.FILES)
        if portForm.is_valid():
            portForm.about_id = form.about_id
            portForm.save()
        
        reviewForm = ReviewForm(request.POST, request.FILES)
        if reviewForm.is_valid():
            reviewForm.about_id = form.about_id
            reviewForm.save()
        
        eventForm = EventForm(request.POST, request.FILES)
        if eventForm.is_valid():
            eventForm.about_id = form.about_id
            eventForm.save()
            return redirect('index')
    else:
        form = AboutForm()
        portForm = PortfolioItemForm()
        reviewForm = ReviewForm()
        eventForm = EventForm()

    context = {"data":{
               "img":"img/slider-img.png",'aboutForm': form,"portForm":portForm, 'reviewForm':reviewForm, 'eventForm':eventForm}}

    
    return render(request, 'about.html', context)

