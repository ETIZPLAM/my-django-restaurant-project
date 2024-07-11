from django.contrib import admin
from .models import Dish


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # افزودن تصویر به نمایش لیست


admin.site.register(Dish, DishAdmin)
