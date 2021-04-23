# Generated by Django 3.1.2 on 2021-04-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[(0, 'educational'), (1, 'novel'), (2, 'magazine'), (3, 'other')], default=3, max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
