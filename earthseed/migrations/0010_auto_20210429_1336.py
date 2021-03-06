# Generated by Django 3.2 on 2021-04-29 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthseed', '0009_alter_forum_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='reply',
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.ManyToManyField(to='earthseed.Topic'),
        ),
        migrations.AddField(
            model_name='topic',
            name='forum',
            field=models.ManyToManyField(to='earthseed.Forum'),
        ),
    ]
