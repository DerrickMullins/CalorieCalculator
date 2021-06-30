from django.db import models
from django.contrib.auth.models import User

# create your models here

class Food(models.Model):
	name = models.CharField(max_length=100)
	carbs = models.FloatField()
	protein = models.FloatField()
	fats = models.FloatField()
	satFats = models.FloatField()
	calories = models.IntegerField()

	def __str__(self):
		return self.name


class Consume(models.Model):
	# ForeignKey = many to many relationship
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)