from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from faject.models import Servise, Category, HowDoWork, OurTerms,Advantages, ServiceDesctiption


class ServiceDesctiptionSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=ServiceDesctiption)

    class Meta:
        model = ServiceDesctiption
        fields = ["id", "title", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }

class AdvantagesSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Advantages)

    class Meta:
        model = Advantages
        fields = ["id", "description", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class HowDoWorkSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=HowDoWork)

    class Meta:
        model = HowDoWork
        fields = ["id", "title", "description", "image", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class OurTermsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=OurTerms)

    class Meta:
        model = OurTerms
        fields = ["id", "title", "description", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


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
    service = HowDoWorkSerializer(many=True, read_only=True)
    out_terms = OurTermsSerializer(many=True, read_only=True)
    advantages = AdvantagesSerializer(many=True, read_only=True)
    descriptions = ServiceDesctiptionSerializer(many=True, read_only=True)

    class Meta:
        model = Servise
        fields = ["id", "title", "short_title",  "short_description", "icon", "image", "category", "service", "descriptions", "out_terms", "advantages", "create_at", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }