# Generated by Django 3.2 on 2021-04-30 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earthseed', '0013_auto_20210430_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='earthseed.book'),
        ),
    ]
