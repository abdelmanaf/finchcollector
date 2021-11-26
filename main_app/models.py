from django.db import models
from django.db.models.enums import Choices
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

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
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1, 
    choices = MEALS, 
    default=MEALS[0][0]
  )

  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']
  
  
