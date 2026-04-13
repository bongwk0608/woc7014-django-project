from django.db import models
from django.template.defaultfilters import slugify


class Tags(models.Model):
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label


class Game(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=50, blank=True, null=True)
    label_tag = models.ManyToManyField(Tags)
    slug = models.SlugField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
        # Generate slug only once when the object is first created
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
        # Ensure consistency by generating slug from review content (first 50 characters)
        if not self.slug:
            self.slug = slugify(self.review[:50])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.review[:50]