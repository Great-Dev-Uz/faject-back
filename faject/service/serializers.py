from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from faject.models import Servise, Category


class CategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)

    class Meta:
        model = Category
        fields = ["id", "name", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class SericeSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Servise)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Servise
        fields = ["id", "title", "description", "image", "category", "create_at", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }