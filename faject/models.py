from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
from django_ckeditor_5.fields import CKEditor5Field


class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Услуга Категория")
        verbose_name_plural = _("Услуга Категория")

    def __str__(self):
        return self.name 


class SubCategory(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("name"), max_length=250),
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
        title = models.CharField(_("Заголовок"), max_length=250),
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
        name = models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Проекта Категория")
        verbose_name_plural = _("Проекта Категория ")

    def __str__(self):
        return self.name 


class Projects(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Заголовок"), max_length=250),
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
        name = models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Блог Категория")
        verbose_name_plural = _("Блог Категория")

    def __str__(self):
        return self.name
    

class BlogSubCategory(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("name"), max_length=250),
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
        title = models.CharField(_("Заголовок"), max_length=250),
        short_description = CKEditor5Field(config_name='extends', verbose_name="Краткое описание"),
        description = CKEditor5Field(config_name='extends', verbose_name="Описание" )
    )
    image = models.ImageField(upload_to='blog/', verbose_name="Изображение")
    category = models.ForeignKey(BlogSubCategory, on_delete=models.CASCADE, verbose_name='Категория')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Блог")
        verbose_name_plural = _("Блог")

    def __str__(self):
        return self.title
    

class Comanda(TranslatableModel):
    translations = TranslatedFields(
        full_name = models.CharField(_("Ф.И.О"), max_length=250),
        position = models.CharField(_("Позиция"), max_length=250),
    )
    image = models.ImageField(upload_to='comanda/', verbose_name="Изображение")


    class Meta:
        ordering = ["-id"]
        verbose_name = _("Команда")
        verbose_name_plural = _("Команда")

    def __str__(self):
        return self.full_clean


class ToolsCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Инструменты Категория")
        verbose_name_plural = _("Инструменты Категория")

    def __str__(self):
        return self.name
    

class Tools(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    category = models.ForeignKey(ToolsCategory, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.ImageField(upload_to='tools', verbose_name="Изображение")

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Инструменты")
        verbose_name_plural = _("Инструменты")

    def __str__(self):
        return self.name


class Application(models.Model):
    full_name = models.CharField(max_length=250, verbose_name="Имя")
    phone = models.CharField(max_length=250, verbose_name="Телефон")
    email = models.EmailField(verbose_name="E-mail")
    service_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Услугу")
    description = models.TextField(verbose_name="Опишите свой проект")
    create_at = models.DateField(auto_now_add=True,  verbose_name="Дата")

    class Meta:
        ordering = ["-id"]
        verbose_name = _("ОСТАВЬТЕ ЗАЯВКУ")
        verbose_name_plural = _("ОСТАВЬТЕ ЗАЯВКУ")

    def __str__(self):
        return self.full_name