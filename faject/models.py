from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields
from django_ckeditor_5.fields import CKEditor5Field


class MainCategory(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["id"]
        verbose_name = _("Основная категория")
        verbose_name_plural = _("Основная категория")

    def __str__(self):
        return self.name 


class MainContent(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Заголовок"), max_length=250),
        description = models.TextField(verbose_name='Описание')
    )
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE,  verbose_name='Категория')

    class Meta:
        ordering = ["id"]
        verbose_name = _("Основное описание")
        verbose_name_plural = _("Основное описание")

    def __str__(self):
        return self.title


class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["id"]
        verbose_name = _("Услуга Категория")
        verbose_name_plural = _("Услуга Категория")

    def __str__(self):
        return self.name 


class Servise(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Заголовок"), max_length=250),
        short_title = models.CharField(max_length=250, null=True, blank=True, verbose_name='Короткое название'),
        short_description = models.TextField(null=True, blank=True, verbose_name='Краткое описание'),
    )
    icon = models.FileField(upload_to='service_icon/', null=True, blank=True, verbose_name='Икона')
    image = models.FileField(upload_to='service/', verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='categorys')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуга")

    def __str__(self):
        return self.title


class ServiceDesctiption(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Заголовок"), max_length=250),
    )
    service = models.ForeignKey(Servise, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Услуга', related_name='descriptions')

    class Meta:
        ordering = ["id"]
        verbose_name = _("Описание услуги")
        verbose_name_plural = _("Описание услуги")

    def __str__(self):
        return self.title


class HowDoWork(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(null=True, blank=True, max_length=250, verbose_name="Заголовок"),
        description = models.TextField(null=True, blank=True, verbose_name="Описание")
    )
    image = models.ImageField(upload_to='service/', null=True, blank=True, verbose_name="Изображение")
    service = models.ForeignKey(Servise, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Услуга', related_name='service')

    class Meta:
        ordering = ["id"]
        verbose_name = _("КАК МЫ РАБОТАЕМ")
        verbose_name_plural = _("КАК МЫ РАБОТАЕМ")

    def __str__(self):
        return self.title


class OurTerms(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(null=True, blank=True, max_length=250, verbose_name="Заголовок"),
        description = models.CharField(null=True, blank=True, max_length=250, verbose_name="Описание")
    )
    service = models.ForeignKey(Servise, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Услуга', related_name='out_terms')

    class Meta:
        ordering = ["id"]
        verbose_name = _("НАШИ УСЛОВИЯ")
        verbose_name_plural = _("НАШИ УСЛОВИЯ")

    def __str__(self):
        return self.title


class Advantages(TranslatableModel):
    translations = TranslatedFields(
        description = models.CharField(null=True, blank=True, max_length=250, verbose_name="Описание")
    )
    service = models.ForeignKey(Servise, on_delete=models.CASCADE, verbose_name='Услуга', related_name='advantages')

    class Meta:
        ordering = ["id"]
        verbose_name = _("ПРЕИМУЩЕСТВА")
        verbose_name_plural = _("ПРЕИМУЩЕСТВА")

    def __str__(self):
        return self.description


class ProjectCategory(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["id"]
        verbose_name = _("Проекта Категория")
        verbose_name_plural = _("Проекта Категория ")

    def __str__(self):
        return self.name 


class Projects(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Заголовок"), max_length=250),
        short_description = CKEditor5Field(config_name='extends', verbose_name="Краткое описание"),
        description = CKEditor5Field(config_name='extends', verbose_name="Описание" )
    )
    image = models.ImageField(upload_to='projects/', verbose_name="Изображение")
    category_service = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория услуг')
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, verbose_name='Категория')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Проекты")
        verbose_name_plural = _("Проекты")

    def __str__(self):
        return self.title


class BlogCategory(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["id"]
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
        ordering = ["id"]
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
        ordering = ["id"]
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
        ordering = ["id"]
        verbose_name = _("Команда")
        verbose_name_plural = _("Команда")

    def __str__(self):
        return self.full_name


class ToolsCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")

    class Meta:
        ordering = ["id"]
        verbose_name = _("Инструменты Категория")
        verbose_name_plural = _("Инструменты Категория")

    def __str__(self):
        return self.name
    

class Tools(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    category = models.ForeignKey(ToolsCategory, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.ImageField(upload_to='tools', verbose_name="Изображение")

    class Meta:
        ordering = ["id"]
        verbose_name = _("Инструменты")
        verbose_name_plural = _("Инструменты")

    def __str__(self):
        return self.name


class Application(models.Model):
    full_name = models.CharField(max_length=250, verbose_name="Имя")
    phone = models.CharField(max_length=250, verbose_name="Телефон")
    email = models.EmailField(verbose_name="E-mail")
    service_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Услугу")
    description = models.TextField(verbose_name="Опишите свой проект")
    create_at = models.DateField(auto_now_add=True,  verbose_name="Дата")

    class Meta:
        ordering = ["id"]
        verbose_name = _("ОСТАВЬТЕ ЗАЯВКУ")
        verbose_name_plural = _("ОСТАВЬТЕ ЗАЯВКУ")

    def __str__(self):
        return self.full_name