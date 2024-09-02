from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from faject.models import Category, Servise

class SeriSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Servise)

    class Meta:
        model = Servise
        fields = ["id", "short_title", "icon", "translations"]

    def get_text(self, instance):
        return {    
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class CategorySerializers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)
    categorys = SeriSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "categorys", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }
