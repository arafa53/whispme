# Generated by Django 3.1.4 on 2021-03-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whispme', '0004_remove_postcomment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='myphoto/')),
                ('content', models.TextField()),
            ],
        ),
    ]