# Generated by Django 4.1.7 on 2023-03-24 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_event_about_id_alter_portfolioitem_about_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='about',
            name='facebook_ID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='about',
            name='github_ID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin_ID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='about',
            name='twitter_ID',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
