from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from faject.models import Category, SubCategory
from faject.category.serializers import CategorySerializers, SubCategorySerializer


class CategoryView(APIView):

    @swagger_auto_schema(tags=['Category'], responses={200: CategorySerializers(many=True)})
    def get(self, request):
        instance = Category.objects.all()
        serializer = CategorySerializers(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 
    

class SubCategoryView(APIView):

    @swagger_auto_schema(tags=['Category'], responses={200: SubCategorySerializer(many=True)})
    def get(self, request):
        instance = SubCategory.objects.all()
        serializer = SubCategorySerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 