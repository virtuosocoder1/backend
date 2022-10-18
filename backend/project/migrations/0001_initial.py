# Generated by Django 3.2.9 on 2022-10-15 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_id', models.IntegerField(unique=True)),
                ('number', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=100)),
                ('seat', models.IntegerField()),
                ('song', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('ques1', models.IntegerField()),
                ('ques2', models.IntegerField()),
                ('alldone', models.IntegerField()),
            ],
            options={
                'db_table': 'club',
                'managed': False,
            },
        ),
    ]
