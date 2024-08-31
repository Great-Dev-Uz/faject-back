from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from faject.models import MainCategory, MainContent
from faject.main.serializers import MainCategorySerializer, MainContentSerializer


class MainCategorysView(APIView):

    @swagger_auto_schema(tags=['Main'], responses={200: MainCategorySerializer(many=True)})
    def get(self, request):
        instances = MainCategory.objects.all()
        serializer = MainCategorySerializer(instances, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class MainContentsView(APIView):

    @swagger_auto_schema(tags=['Main'], responses={200: MainContentSerializer(many=True)})
    def get(self, request):
        instances = MainContent.objects.all()
        serializer = MainContentSerializer(instances, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class MainContentCategoryView(APIView):

    @swagger_auto_schema(tags=['Main'], responses={200: MainContentSerializer(many=True)})
    def get(self, request, pk):
        instances = MainContent.objects.filter(category=pk)
        serializer = MainContentSerializer(instances, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)