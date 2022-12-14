# Generated by Django 3.0 on 2022-07-03 10:16

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
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
