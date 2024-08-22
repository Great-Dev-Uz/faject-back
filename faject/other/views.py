from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from faject.models import Comanda, ToolsCategory, Tools, Application
from faject.other.serializers import ComandaSerializer, ToolsCategorySerializer, ToolsSerializer, ApplicationSerializer


class ComandaView(APIView):

    @swagger_auto_schema(tags=['Other'], responses={200: ComandaSerializer(many=True)})
    def get(self, request):
        instance = Comanda.objects.all()
        serializer = ComandaSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 


class ToolsCategoryView(APIView):

    @swagger_auto_schema(tags=['Other'], responses={200: ToolsCategorySerializer(many=True)})
    def get(self, request):
        instance = ToolsCategory.objects.all()
        serializer = ToolsCategorySerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 


class ToolsView(APIView):

    @swagger_auto_schema(tags=['Other'], responses={200: ToolsSerializer(many=True)})
    def get(self, request):
        instance = Tools.objects.all()
        serializer = ToolsSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 


class ToolView(APIView):

    @swagger_auto_schema(tags=['Other'], responses={200: ToolsSerializer(many=True)})
    def get(self, request, pk):
        instance = Tools.objects.filter(category=pk)
        serializer = ToolsSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 


class ApplicationView(APIView):

    @swagger_auto_schema(
        tags=['Other'],
        request_body=ApplicationSerializer
    )
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success send'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
