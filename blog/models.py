from django.db import models
from django.urls import reverse


class Blog(models.Model):

    image = models.ImageField(
        upload_to="images/")
    image2 = models.ImageField(upload_to="images/", blank=True)
    image3 = models.ImageField(upload_to="images/", blank=True)
    text = models.TextField()
    text2 = models.TextField(blank=True)
    text3 = models.TextField(blank=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=250)

    def summary(self):
        return self.text[:200]

    def pub_date_pretty(self):
        return self.date.strftime("%b %e %Y")

    def __str__(self):
        return self.title


""" class User_Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:post_detail", kwargs={"id": self.id})
 """
