from django.conf import settings
from django.db import models

class Computer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.book

class Electronics(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.book

class Electrical(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.book

class Mechanical(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.book