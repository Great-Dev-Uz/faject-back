from django.urls import path
from faject.category.views import CategoryView, SubCategoryView
from faject.service.views import ServicesView, ServiceCategoryView, ServiceSubCategoryView, ServiceView
from faject.projects.views import ProjectCategoryView, ProjectsView, ProjectsCategorView, ProjectView
from faject.blog.views import BlogCategoryView, BlogSubCategoryView, BlogsView, BlogsCategoryView, BlogsSubCategoryView, BlogView


urlpatterns = [
    # Category
    path('category/', CategoryView.as_view()),
    path('sub/category/', SubCategoryView.as_view()),
    # Service
    path('service/', ServicesView.as_view()),
    path('service/category/<int:pk>/', ServiceCategoryView.as_view()),
    path('service/sub/category/<int:pk>/', ServiceSubCategoryView.as_view()),
    path('service/<int:pk>/', ServiceView.as_view()),
    # Project
    path('project/category/', ProjectCategoryView.as_view()),
    path('project/', ProjectsView.as_view()),
    path('project/category/<int:pk>/', ProjectsCategorView.as_view()),
    path('project/<int:pk>/', ProjectView.as_view()),
    # Blog
    path('blog/category/', BlogCategoryView.as_view()),
    path('blog/sub/category/', BlogSubCategoryView.as_view()),
    path('blog/', BlogsView.as_view()),
    path('blog/<int:pk>/', BlogView.as_view()),
    path('blog/category/<int:pk>/', BlogsCategoryView.as_view()),
    path('blog/sub/category/<int:pk>/', BlogsSubCategoryView.as_view()),


]