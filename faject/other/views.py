from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from faject.models import Comanda, ToolsCategory, Tools, Application
from faject.other.serializers import ComandaSerializer, ToolsCategorySerializer, ToolsSerializer


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
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'full_name': openapi.Schema(type=openapi.TYPE_STRING, description='full_name'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description='phone'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='email'),
                'service_category': openapi.Schema(type=openapi.TYPE_NUMBER, description='service_category'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='description'),

            }
        )
    )
    def post(self, request):
        full_name = request.data.get('full_name', '')
        phone = request.data.get('phone', '')
        email = request.data.get('email', '')
        service_category = request.data.get('service_category', '')
        description = request.data.get('description', '')
    
        if not full_name:
            return Response({'message': 'Full name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        if not service_category:
            return Response({'message': 'Service category cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        if not phone:
            return Response({'message': 'Phone cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({'message': 'Email cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        if not description:
            return Response({'message': 'Discription cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        concat_user = Application(full_name=full_name, phone=phone, service_category=service_category, email=email, description=description)
        concat_user.save()
        return Response({'message': 'success send'}, status=status.HTTP_201_CREATED)
