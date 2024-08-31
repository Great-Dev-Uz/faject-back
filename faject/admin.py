from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from django.utils.safestring import mark_safe

from faject.models import (
    Category, Servise, HowDoWork, OurTerms,
    ProjectCategory, Projects,
    BlogCategory, BlogSubCategory, Blog,
    Comanda, ToolsCategory, Tools, Application,
    MainCategory, MainContent
)


@admin.register(MainCategory)
class MainCategoryAdmin(TranslatableAdmin):
    list_display = ["name"]


@admin.register(MainContent)
class MainContentAdmin(TranslatableAdmin):
    list_display = ["title"]


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ["name"]


@admin.register(Servise)
class ServiseAdmin(TranslatableAdmin):
    list_display = ['title']


@admin.register(HowDoWork)
class HowDoWorkAdmin(TranslatableAdmin):
    list_display = ['title']

@admin.register(OurTerms)
class OurTermsAdmin(TranslatableAdmin):
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