from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from faject.pagination import ProductPagination
from faject.models import BlogCategory, BlogSubCategory, Blog
from faject.blog.serializers import BlogCategorySerializer, BlogSubCategorySerializer, BlogSerializer


class BlogCategoryView(APIView):

    @swagger_auto_schema(tags=['Blog'], responses={200: BlogCategorySerializer(many=True)})
    def get(self, request):
        instance = BlogCategory.objects.all()
        serializer = BlogCategorySerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK) 


class BlogSubCategoryView(APIView):

    @swagger_auto_schema(tags=['Blog'], responses={200: BlogSubCategorySerializer(many=True)})
    def get(self, request):
        instance = BlogSubCategory.objects.all()
        serializer = BlogSubCategorySerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogsView(APIView):
    pagination_class = ProductPagination

    @swagger_auto_schema(tags=['Blog'], responses={200: BlogSerializer(many=True)})
    def get(self, request):
        instances = Blog.objects.all()
        paginator = self.pagination_class()
        paginated_instances = paginator.paginate_queryset(instances, request)
        serializer = BlogSerializer(paginated_instances, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class BlogsCategoryView(APIView):
    pagination_class = ProductPagination

    @swagger_auto_schema(tags=['Blog'], responses={200: BlogSerializer(many=True)})
    def get(self, request, pk):
        instances = Blog.objects.filter(category=pk)
        paginator = self.pagination_class()
        paginated_instances = paginator.paginate_queryset(instances, request)
        serializer = BlogSerializer(paginated_instances, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class BlogsSubCategoryView(APIView):
    pagination_class = ProductPagination

    @swagger_auto_schema(tags=['Blog'], responses={200: BlogSerializer(many=True)})
    def get(self, request, pk):
        instances = Blog.objects.filter(category__category=pk)
        paginator = self.pagination_class()
        paginated_instances = paginator.paginate_queryset(instances, request)
        serializer = BlogSerializer(paginated_instances, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    

class BlogView(APIView):

    @swagger_auto_schema(tags=['Blog'], responses={200: BlogSerializer(many=True)})
    def get(self, request, pk):
        instances = get_object_or_404(Blog, id=pk)
        serializer = BlogSerializer(instances, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
