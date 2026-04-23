from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PhoneModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    phone_model = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    content = models.TextField()


class NewsLink(models.Model):
    phone_model = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    url = models.URLField()