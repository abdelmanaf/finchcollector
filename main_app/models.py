from django.db import models
from django.urls import reverse

class Finch(models.Model):
  name = models.CharField(max_length=100, null=True)
  breed = models.CharField(max_length=100, null=True)
  description = models.TextField(max_length=250, null=True)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("finches_detail", kwargs={"finch_id": self.id})

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(max_length=1)
  
