from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from faject.models import Category
from faject.category.serializers import CategorySerializers


class CategoryView(APIView):

    @swagger_auto_schema(tags=['Category'], responses={200: CategorySerializers(many=True)})
    def get(self, request):
        instance = Category.objects.all()
        serializer = CategorySerializers(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 
