# Generated by Django 4.2.dev20220519083822 on 2022-05-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_choice_options_alter_question_options_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='question',
        ),
        migrations.AddField(
            model_name='poll',
            name='question',
            field=models.ManyToManyField(to='polls.question'),
        ),
    ]
