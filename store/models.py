from django.conf import settings
from django.db import models

class Python(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class Java(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class Csharp(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class Cplus(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class C(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class Ruby(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class PHP(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class Electrical(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class Electronics(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class Mechanical(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title

class Civil(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(default=True)

    def __str__(self):
        return self.title