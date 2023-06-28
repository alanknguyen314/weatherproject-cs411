from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class VisitedList(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()

  def get_absolute_url(self):
      return reverse("visited-list-detail", kwargs={"pk": self.pk})

  def __str__(self):
    return self.title