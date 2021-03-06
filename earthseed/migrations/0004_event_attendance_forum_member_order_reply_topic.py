# Generated by Django 3.2 on 2021-04-18 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earthseed', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='earthseed.book')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=24)),
                ('last_name', models.CharField(max_length=24)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=24)),
                ('password', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('forum_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='earthseed.forum')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='earthseed.member')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earthseed.member')),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earthseed.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('date', models.DateField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='earthseed.book')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='earthseed.member')),
            ],
        ),
        migrations.CreateModel(
            name='Event_Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='earthseed.event')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='earthseed.member')),
            ],
        ),
    ]
