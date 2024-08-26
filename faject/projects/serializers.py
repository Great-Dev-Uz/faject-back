from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from faject.models import ProjectCategory, Projects


class ProjectCategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=ProjectCategory)

    class Meta:
        model = ProjectCategory
        fields = ["id", "name", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class ProjectSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Projects)
    category = ProjectCategorySerializer(read_only=True)

    class Meta:
        model = Projects
        fields = ["id", "title", "short_description", "description", "image", "category", "create_at", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }