import random
import string
from django.forms import formset_factory
from django.shortcuts import render
from .models import About, Review, Event, PortfolioItem

from django.shortcuts import render, redirect
from .models import About, Review, Event, PortfolioItem, User
from .forms import AboutForm, ReviewForm, EventForm, PortfolioItemForm


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login as do_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

import time
# Create your views here.

@login_required
def index(request,id):
    a = About.objects.get(id=id)
    r = Review.objects.filter(about_id=a.id)
    e = Event.objects.filter(about_id=a.id)
    p = PortfolioItem.objects.filter(about_id=a.id)
    for x in e:
        date_obj = x.date
        x.date = date_obj.strftime("%d/%m/%Y")
        x.year = date_obj.strftime("%Y")
        x.day = date_obj.strftime("%d")
        if 4 <= int(x.day) <= 20 or 24 <= int(x.day) <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][int(x.day) % 10 - 1]
        x.day = x.day + suffix
        x.comp_date = f"{x.day} {date_obj.strftime('%b')}, {x.year}"

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

def home(request):
    context = {"user":request.user}
    return render(request, "home.html",context)
def login(request):
    context = {'type': 'login'}
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('profile')
        else:
            context.update({"error": True})
    else:
        form = AuthenticationForm()

    for field in form.fields:
        form.fields[field].widget.attrs.update({"placeholder": ""})
    context.update({"form": form})
    return render(request, "login.html",context)
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect("login")
    context = {"form":form}
    return render(request, "register.html",context)

@login_required
def profile(request):
    context = {"user":request.user}
    return render(request, "profile.html",context)

@login_required
def confirmation(request):
    if request.method == "POST":
        portText = request.method.get("portText")
        reviewText = request.method.get("reviewText")
        eventText = request.method.get("eventText")

        return redirect("form",portText,reviewText,eventText)
    return render(request, "confirm.html")

@login_required
def form(request, port,review, event):
    portNum = port
    reviewNum = review
    eventNum = event

    form = AboutForm(prefix='aboutForm')
    portFormSet = formset_factory(PortfolioItemForm, extra=portNum)
    reviewFormSet = formset_factory(ReviewForm, extra=reviewNum)
    eventFormSet = formset_factory(EventForm, extra=eventNum)

    portForm = portFormSet(prefix='portForm')
    reviewForm = reviewFormSet(prefix='reviewForm')
    eventForm = eventFormSet(prefix='eventForm')

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

        portForm = portFormSet(request.POST, request.FILES, prefix='portForm')
        if portForm.is_valid():
            for form in portForm:
                print(form.cleaned_data)
                obj = form.save(commit=False)
                obj.about_id = id
                obj.save()
            c+=1
            context['portForm'] = portForm
        
        reviewForm = reviewFormSet(request.POST, request.FILES,  prefix='reviewForm')
        if reviewForm.is_valid():
            for form in reviewForm:
                obj = form.save(commit=False)
                obj.about_id = id
                obj.save()
            c+=1
            context['reviewForm'] = reviewForm
        
        eventForm = eventFormSet(request.POST, request.FILES, prefix='eventForm')
        if eventForm.is_valid():
            for form in eventForm:
                obj = form.save(commit=False)
                obj.about_id = id
                obj.save()
            c+=1
            context['eventForm'] = eventForm

        if c == 4:
            user_obj = User(portfolioIDs = {time.time():id})
            return redirect('index',id)
    
    return render(request, 'about.html', context)

