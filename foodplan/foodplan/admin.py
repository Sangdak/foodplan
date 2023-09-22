from django.contrib import admin

from .models import Culinary, Allergen, Category, Ingredient, \
                    Food, ImageFood, Term


@admin.register(Culinary)
class CulinaryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'image',
    ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'allergen',
        'category',
        'price',
        'image',
        'caloric',
    ]


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'culinary',
        'recipe',
    ]


@admin.register(ImageFood)
class ImageFoodAdmin(admin.ModelAdmin):
    list_display = [
        'image',
        'food',
    ]


@admin.register(Term)
class TermdAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'discount',
    ]
