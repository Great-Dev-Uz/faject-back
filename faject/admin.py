from django.contrib import admin
from parler.admin import TranslatableAdmin
from faject.models import Category, SubCategory


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ["name"]


@admin.register(SubCategory)
class SubCategoryAdmin(TranslatableAdmin):
    list_display = ['name']