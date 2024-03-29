# Generated by Django 2.1.7 on 2019-12-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Civil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='string', max_length=200)),
                ('bookname', models.CharField(default='string', max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='string', max_length=200)),
                ('bookname', models.CharField(default='string', max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Electrical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='string', max_length=200)),
                ('bookname', models.CharField(default='string', max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='string', max_length=200)),
                ('bookname', models.CharField(default='string', max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='string', max_length=200)),
                ('bookname', models.CharField(default='string', max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField(default=True)),
            ],
        ),
    ]
