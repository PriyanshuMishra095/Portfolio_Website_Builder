# Generated by Django 4.1.7 on 2023-03-24 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_about_email_about_facebook_id_about_github_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='email',
        ),
        migrations.RemoveField(
            model_name='about',
            name='facebook_ID',
        ),
        migrations.RemoveField(
            model_name='about',
            name='github_ID',
        ),
        migrations.RemoveField(
            model_name='about',
            name='linkedin_ID',
        ),
        migrations.RemoveField(
            model_name='about',
            name='twitter_ID',
        ),
    ]