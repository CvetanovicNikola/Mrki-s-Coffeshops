from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile


class Coffeeshop(models.Model):
    SMOKING_CHOICES = [("Y", "Yes"), ("N", "No")]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    smoking = models.CharField(choices=SMOKING_CHOICES, max_length=1)
    description = models.TextField()
    description2 = models.TextField(blank=True)
    description3 = models.TextField(blank=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    image1 = models.ImageField(upload_to="images")
    image2 = models.ImageField(upload_to="images", blank=True)
    image3 = models.ImageField(upload_to="images", blank=True)
    votes = models.IntegerField(default=0)
    voted = models.TextField(blank=True)
    working_hours_weekdays = models.CharField(max_length=20, blank=True)
    working_hours_saturday = models.CharField(max_length=20, blank=True)
    working_hours_sunday = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    def summary(self):
        return self.description[:100]

    def date_pretty(self):
        return self.date.strftime("%b %e %Y")

    def get_absolute_url(self):
        return reverse("coffeshop_detail", kwargs={"pk": self.pk})
