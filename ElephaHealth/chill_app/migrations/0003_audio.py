# Generated by Django 4.2.3 on 2023-07-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chill_app', '0002_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=30)),
                ('link', models.URLField()),
            ],
        ),
    ]
