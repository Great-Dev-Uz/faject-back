from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=250),
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Категория")
        verbose_name_plural = _("Категория")

    def __str__(self):
        return self.name 


class SubCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=250),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='category')

    class Meta:
        ordering = ["-id"]
        verbose_name = _("Подкатегория")
        verbose_name_plural = _("Подкатегория")

    def __str__(self):
        return self.name 