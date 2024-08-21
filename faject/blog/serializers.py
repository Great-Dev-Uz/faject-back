from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from faject.models import BlogCategory, BlogSubCategory, Blog


class BlogSubCategorySer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=BlogSubCategory)

    class Meta:
        model = BlogSubCategory
        fields = ["id", "name", "category", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class BlogCategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=BlogCategory)
    blog_categor = BlogSubCategorySer(many=True)

    class Meta:
        model = BlogCategory
        fields = ["id", "name", "blog_categor", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class BlogSubCategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=BlogSubCategory)
    category = BlogCategorySerializer(read_only=True)

    class Meta:
        model = BlogSubCategory
        fields = ["id", "name", "category", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }


class BlogSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Blog)
    category = BlogSubCategorySerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "short_description", "description", "image", "category", "create_at", "translations"]

    def get_text(self, instance):
        return {
            "ru": instance.name_ru,
            "en": instance.name_en,
            "uz": instance.name_uz,
        }