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
