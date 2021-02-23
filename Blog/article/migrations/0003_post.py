# Generated by Django 3.1.6 on 2021-02-23 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0002_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
