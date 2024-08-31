from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from faject.models import MainCategory, MainContent


class MainCategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=MainCategory)

    class Meta:
        model = MainCategory
        fields = ["id", "name", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class MainContentSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=MainContent)

    class Meta:
        model = MainContent
        fields = ["id", "title", "description", "category", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }