from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='dish_images/',
                              blank=True, null=True)  # افزودن فیلد تصویر

    def str(self):
        return self.name


# Create your models here.
