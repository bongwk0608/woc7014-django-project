from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    since = models.IntegerField()

    def __str__(self):
        return self.name


class PhoneModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    launch_date = models.DateField()
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name


class Review(models.Model):
    phone = models.ManyToManyField(PhoneModel)
    content = models.TextField()
    date_published = models.DateField(auto_now=True)

    def __str__(self):
        return self.content[:50]