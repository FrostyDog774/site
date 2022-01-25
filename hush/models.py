from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(null=True)
    image1 = models.ImageField(upload_to='media/images/', blank=True)
    image2 = models.ImageField(upload_to='media/images/', blank=True)
    image3 = models.ImageField(upload_to='media/images/', blank=True)
    image4 = models.ImageField(upload_to='media/images/', blank=True)
    instagram = models.TextField(max_length=100, null=True, blank=True)
    tiktok = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
