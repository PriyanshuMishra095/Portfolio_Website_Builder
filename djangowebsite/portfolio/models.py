from django.db import models

# Create your models here.

class About(models.Model):
    icon = models.FileField(upload_to='static/img')
    logo = models.FileField(upload_to='static/img')
    name = models.CharField(max_length=300)
    about = models.CharField(max_length=300)
    work_title = models.CharField(max_length=300)
    work_desc = models.CharField(max_length=300)
    experience_years = models.CharField(max_length=300)
    skill_1_title = models.CharField(max_length=300)
    skill_1_desc = models.CharField(max_length=300)
    skill_2_title = models.CharField(max_length=300)
    skill_2_desc = models.CharField(max_length=300)
    skill_3_title = models.CharField(max_length=300)
    skill_3_desc = models.CharField(max_length=300)
    skill_4_title = models.CharField(max_length=300)
    skill_4_desc = models.CharField(max_length=300)
    talent_1_title = models.CharField(max_length=300)
    talent_1_perc = models.IntegerField()
    talent_2_title = models.CharField(max_length=300)
    talent_2_perc = models.IntegerField()
    talent_3_title = models.CharField(max_length=300)
    talent_3_perc = models.IntegerField()
    age = models.IntegerField()
    insta_ID = models.CharField(max_length=100)

class Review(models.Model):
    about_id = models.ForeignKey(About, models.CASCADE)
    comment = models.CharField(max_length=300)
    image = models.FileField(upload_to='static/img')
    name = models.CharField(max_length=300)

class Event(models.Model):
    about_id = models.ForeignKey(About, models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=300)
    desc_1 = models.CharField(max_length=1000)
    desc_2 = models.CharField(max_length=1000)

class PortfolioItem(models.Model):
    about_id = models.ForeignKey(About, models.CASCADE)
    image = models.FileField(upload_to='static/img')
    image_desc = models.CharField(max_length=100) 
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=300) 