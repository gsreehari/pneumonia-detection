# Generated by Django 3.0.2 on 2021-06-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='user_xray_images')),
                ('result', models.CharField(max_length=100)),
            ],
        ),
    ]
