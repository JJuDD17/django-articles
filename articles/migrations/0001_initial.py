# Generated by Django 3.0.2 on 2020-02-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField()),
                ('author_name', models.CharField(default='Somebody', max_length=32)),
                ('article_text', models.CharField(max_length=5000)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
