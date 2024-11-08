from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from faject.pagination import ProductPagination
from faject.models import Servise, Projects
from faject.service.serializers import SericeSerializer
from faject.projects.serializers import ProjectSerializer


class ServicesView(APIView):
    pagination_class = ProductPagination

    @swagger_auto_schema(tags=['Service'], responses={200: SericeSerializer(many=True)})
    def get(self, request):
        instances = Servise.objects.all()
        paginator = self.pagination_class()
        paginated_instances = paginator.paginate_queryset(instances, request)
        serializer = SericeSerializer(paginated_instances, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class ServiceCategoryView(APIView):
    pagination_class = ProductPagination

    @swagger_auto_schema(tags=['Service'], responses={200: SericeSerializer(many=True)})
    def get(self, request, pk):
        instances = Servise.objects.filter(category=pk)
        paginator = self.pagination_class()
        paginated_instances = paginator.paginate_queryset(instances, request)
        serializer = SericeSerializer(paginated_instances, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    

class ServiceView(APIView):

    @swagger_auto_schema(tags=['Service'], responses={200: SericeSerializer(many=True)})
    def get(self, request, pk):
        instances = get_object_or_404(Servise, id=pk)
        project = Projects.objects.filter(category_service=instances.category)
        serializer_project = ProjectSerializer(project, many=True, context={'request':request})
        serializer = SericeSerializer(instances, context={'request': request})
        return Response({'serivce': serializer.data, 'project': serializer_project.data}, status=status.HTTP_200_OK)