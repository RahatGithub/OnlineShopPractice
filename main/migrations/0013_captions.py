# Generated by Django 3.2.4 on 2022-03-02 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_order_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Captions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(default='', upload_to='main/images')),
            ],
        ),
    ]
