# Generated by Django 4.1.2 on 2022-12-04 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_canvascomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canvascomment',
            name='user',
        ),
        migrations.AddField(
            model_name='canvascomment',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
