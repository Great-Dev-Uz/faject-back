from django.contrib import admin
from parler.admin import TranslatableAdmin
from faject.models import (
    Category, SubCategory, Servise,
    ProjectCategory, Projects,
    BlogCategory, BlogSubCategory, Blog
)


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ["name"]


@admin.register(SubCategory)
class SubCategoryAdmin(TranslatableAdmin):
    list_display = ['name']


@admin.register(Servise)
class ServiseAdmin(TranslatableAdmin):
    list_display = ['title']


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(TranslatableAdmin):
    list_display = ["name"]


@admin.register(Projects)
class ProjectAdmin(TranslatableAdmin):
    list_display = ['title']


@admin.register(BlogCategory)
class BlogCategoryAdmin(TranslatableAdmin):
    list_display = ["name"]

@admin.register(BlogSubCategory)
class BlogSubCategoryAdmin(TranslatableAdmin):
    list_display = ["name"]


@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    list_display = ['title']