from django.contrib import admin
from parler.admin import TranslatableAdmin
from faject.models import (
    Category, SubCategory, Servise,
    ProjectCategory, Projects,
    BlogCategory, BlogSubCategory, Blog,
    Comanda, ToolsCategory, Tools, Application
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



@admin.register(Comanda)
class ComandaAdmin(TranslatableAdmin):
    list_display = ['full_name']

admin.site.register(ToolsCategory)
admin.site.register(Tools)


class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ['full_name', 'phone', 'email', 'service_category', 'description', 'create_at']
    list_display = [ 'id', 'full_name', 'phone', 'create_at']
    search_fields = ['full_name', 'phone', 'create_at']
    list_filter = ['full_name', 'phone', 'create_at']

admin.site.register(Application, ApplicationAdmin)