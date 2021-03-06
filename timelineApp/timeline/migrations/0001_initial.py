# Generated by Django 3.0.2 on 2020-01-10 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Timeline', max_length=50)),
                ('tagged_users', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Event', max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('image', models.ImageField(default='', upload_to='media/')),
                ('timeline_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='timeline.Timeline')),
            ],
        ),
    ]
