# Generated by Django 3.1.3 on 2020-12-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identifiers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier_id', models.CharField(max_length=40)),
                ('identifier_name', models.CharField(max_length=50)),
                ('identifier_type', models.CharField(max_length=30)),
                ('identifier_comment', models.CharField(max_length=250)),
            ],
        ),
    ]
