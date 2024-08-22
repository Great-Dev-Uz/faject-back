from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from rest_framework import serializers

from faject.models import Comanda, ToolsCategory, Tools, Application


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


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['full_name', 'phone', 'email', 'service_category', 'description']

    def validate(self, data):
        if not data.get('full_name'):
            raise serializers.ValidationError({'full_name': 'Full name cannot be empty'})
        if not data.get('phone'):
            raise serializers.ValidationError({'phone': 'Phone cannot be empty'})
        if not data.get('email'):
            raise serializers.ValidationError({'email': 'Email cannot be empty'})
        if not data.get('service_category'):
            raise serializers.ValidationError({'service_category': 'Service category cannot be empty'})
        if not data.get('description'):
            raise serializers.ValidationError({'description': 'Description cannot be empty'})
        return data