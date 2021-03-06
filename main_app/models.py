from django.db import models
from django.db.models.enums import Choices
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Finch(models.Model):
  name = models.CharField(max_length=100, null=True)
  breed = models.CharField(max_length=100, null=True)
  description = models.TextField(max_length=250, null=True)
  age = models.IntegerField()

  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("finches_detail", kwargs={"finch_id": self.id})

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
      #! len( self.feeding_set.filter(date=date.today()) ) same as the one above

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


  
  
