# Generated by Django 3.2 on 2022-04-21 23:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('taps', '0007_alter_tap_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tap',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='date the Link was created', verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tap',
            name='title',
            field=models.CharField(default='The Default Title', help_text='short title for the url item', max_length=200),
        ),
    ]
