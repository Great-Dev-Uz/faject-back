from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from parler.admin import TranslatableTabularInline

from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from faject.models import (
    Category, Servise, HowDoWork, OurTerms, Advantages, ServiceDesctiption,
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


class LimitInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        # count all forms that have not been marked for deletion
        count = sum(1 for form in self.forms if not self._should_delete_form(form))
        max_num = 10  # specify your max number of images here
        if count > max_num:
            raise ValidationError(f'You can only associate up to {max_num} images with this product.')


class ServiceDesctiptionInline(TranslatableTabularInline):
    model = ServiceDesctiption
    formset = LimitInlineFormSet
    extra = 1
    min_num = 1
    max_num = 10
    fields = ['title']


@admin.register(Servise)
class ServiseAdmin(TranslatableAdmin):
    inlines = [
        ServiceDesctiptionInline,
    ]
    list_display = ['title']


@admin.register(HowDoWork)
class HowDoWorkAdmin(TranslatableAdmin):
    list_display = ['title']

@admin.register(OurTerms)
class OurTermsAdmin(TranslatableAdmin):
    list_display = ['title']

@admin.register(Advantages)
class AdvantagesAdmin(TranslatableAdmin):
    list_display = ['description']

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