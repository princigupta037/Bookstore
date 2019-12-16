from django.conf import settings
from django.db import models
from django.utils import timezone


class Computer(models.Model):

    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname

class Electrical(models.Model):

    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname

class Electronic(models.Model):
    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname

class Civil(models.Model):
    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname

class Mechanical(models.Model):
    author = models.CharField(max_length=200, default='string')
    bookname = models.CharField(max_length=200, default='string')
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.bookname