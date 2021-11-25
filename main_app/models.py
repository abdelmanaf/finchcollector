from django.db import models

class Finch(models.Model):
  name = models.CharField(max_length=100, null=True)
  breed = models.CharField(max_length=100, null=True)
  description = models.TextField(max_length=250, null=True)
  age = models.IntegerField()

  def __str__(self):
    return self.name
