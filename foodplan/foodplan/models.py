from django.db import models


class Culinary(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Тип меню')

    class Meta:
        verbose_name = 'Тип меню'
        verbose_name_plural = 'Тип меню'

    def __str__(self):
        return self.title


class Allergen(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Аллерген')

    class Meta:
        verbose_name = 'Аллерген'
        verbose_name_plural = 'Аллергены'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Категория')

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='category_img')

    class Meta:
        verbose_name = 'Категория блюда'
        verbose_name_plural = 'Категории блюд'

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Ингредиент')

    allergen = models.ForeignKey(
        Allergen,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Аллерген',
        related_name='products')

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Категория',
        related_name='products')

    price = models.DecimalField(
        'Цена',
        max_digits=7,
        decimal_places=2)

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='imgs/ingredients')

    caloric = models.IntegerField(
        verbose_name='Калорийность')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.title}, {self.category.title}'


class Food(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Блюдо')

    ingredient = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        related_name='foods')

    culinary = models.ForeignKey(
        Culinary,
        on_delete=models.CASCADE,
        verbose_name='Тип',
        related_name='foods')

    recipe = models.TextField(
        verbose_name='Рецепт')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title


class ImageFood(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='imgs/foods')

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        verbose_name='Блюдо',
        related_name='images')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.food.title
