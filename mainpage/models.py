from django.db import models

class Category(models.Model):
	name = models.CharField("Імя блюда", max_length=20)
	descriptions = models.TextField("Опис блюда")
	image = models.ImageField("Картинка", upload_to="actors/")
	price = models.PositiveIntegerField("Ціна", default=0)

