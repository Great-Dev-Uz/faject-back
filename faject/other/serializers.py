from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from rest_framework import serializers

from faject.models import Comanda, ToolsCategory, Tools


class ComandaSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Comanda)

    class Meta:
        model = Comanda
        fields = ["id", "full_name", "position", "image", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class ToolsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ToolsCategory
        fields = ["id", "name"]


class ToolsSerializer(serializers.ModelSerializer):
    category = ToolsCategorySerializer(read_only=True)

    class Meta:
        model = Tools
        fields = ["id", "name", "category", "image"]