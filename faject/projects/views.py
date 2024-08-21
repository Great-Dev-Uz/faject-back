from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from faject.pagination import ProductPagination
from faject.models import ProjectCategory, Projects
from faject.projects.serializers import ProjectCategorySerializer, ProjectSerializer


class ProjectCategoryView(APIView):

    @swagger_auto_schema(tags=['Project'], responses={200: ProjectCategorySerializer(many=True)})
    def get(self, request):
        instance = ProjectCategory.objects.all()
        serializer = ProjectCategorySerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 


class ProjectsView(APIView):
    pagination_class = ProductPagination

    @swagger_auto_schema(tags=['Project'], responses={200: ProjectSerializer(many=True)})
    def get(self, request):
        instances = Projects.objects.all()
        paginator = self.pagination_class()
        paginated_instances = paginator.paginate_queryset(instances, request)
        serializer = ProjectSerializer(paginated_instances, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class ProjectsCategorView(APIView):
    pagination_class = ProductPagination

    @swagger_auto_schema(tags=['Project'], responses={200: ProjectSerializer(many=True)})
    def get(self, request, pk):
        instances = Projects.objects.filter(category=pk)
        paginator = self.pagination_class()
        paginated_instances = paginator.paginate_queryset(instances, request)
        serializer = ProjectSerializer(paginated_instances, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class ProjectView(APIView):

    @swagger_auto_schema(tags=['Project'], responses={200: ProjectSerializer(many=True)})
    def get(self, request, pk):
        instances = get_object_or_404(Projects, id=pk)
        serializer = ProjectSerializer(instances, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
