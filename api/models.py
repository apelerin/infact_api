from django.db import models
from django.contrib.postgres.fields import ArrayField


class Journal(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    match = ArrayField(models.TextField(), default=list)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    body = models.TextField()
    link = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class InformationHub(models.Model):
    title = models.CharField(max_length=255)
    original_source_link = models.CharField(max_length=255)
    articles = models.ManyToManyField(Article)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
