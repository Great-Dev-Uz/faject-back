from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
from django_ckeditor_5.fields import CKEditor5Field


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Услуга Категория")
        verbose_name_plural = _("Услуга Категория")

    def __str__(self):
        return self.name 


class SubCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=250),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='category')

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Услуга Подкатегория")
        verbose_name_plural = _("Услуга Подкатегория")

    def __str__(self):
        return self.name 
    

class Servise(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Заголовок"), max_length=250),
        description = CKEditor5Field(config_name='extends', verbose_name="Описание" )
    )
    image = models.ImageField(upload_to='service/', verbose_name="Изображение")
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Категория', related_name='categorys')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуга")

    def __str__(self):
        return self.title 


class ProjectCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Проекта Категория")
        verbose_name_plural = _("Проекта Категория ")

    def __str__(self):
        return self.name 


class Projects(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Заголовок"), max_length=250),
        description = CKEditor5Field(config_name='extends', verbose_name="Описание" )
    )
    image = models.ImageField(upload_to='projects/', verbose_name="Изображение")
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, verbose_name='Категория')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Проекты")
        verbose_name_plural = _("Проекты")

    def __str__(self):
        return self.title


class BlogCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Блог Категория")
        verbose_name_plural = _("Блог Категория")

    def __str__(self):
        return self.name
    

class BlogSubCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=250),
    )
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='Категория', related_name='blog_categor')

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Блог Подкатегория")
        verbose_name_plural = _("Блог Подкатегория")

    def __str__(self):
        return self.name 
    

class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Заголовок"), max_length=250),
        short_description = CKEditor5Field(config_name='extends', verbose_name="Краткое описание"),
        description = CKEditor5Field(config_name='extends', verbose_name="Описание" )
    )
    image = models.ImageField(upload_to='blog/', verbose_name="Изображение")
    category = models.ForeignKey(BlogSubCategory, on_delete=models.CASCADE, verbose_name='Категория')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Проекты")
        verbose_name_plural = _("Проекты")

    def __str__(self):
        return self.title