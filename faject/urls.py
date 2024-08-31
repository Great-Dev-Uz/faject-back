from django.urls import path
from faject.category.views import CategoryView
from faject.service.views import ServicesView, ServiceCategoryView, ServiceView
from faject.projects.views import ProjectCategoryView, ProjectsView, ProjectsCategorView, ProjectView
from faject.blog.views import BlogCategoryView, BlogSubCategoryView, BlogsView, BlogsCategoryView, BlogsSubCategoryView, BlogView
from faject.other.views import ComandaView, ToolsCategoryView, ToolsView, ToolView, ApplicationView
from faject.main.views import MainCategorysView, MainContentsView, MainContentCategoryView


urlpatterns = [
    # Category
    path('category/', CategoryView.as_view()),
    # Service
    path('service/', ServicesView.as_view()),
    path('service/category/<int:pk>/', ServiceCategoryView.as_view()),
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
    # other
    path('comanda/', ComandaView.as_view()),
    path('tools/category/', ToolsCategoryView.as_view()),
    path('tools/', ToolsView.as_view()),
    path('tool/<int:pk>/', ToolView.as_view()),
    path('application/', ApplicationView.as_view()),
    # main
    path('main/category/', MainCategorysView.as_view()),
    path('main/content/', MainContentsView.as_view()),
    path('main/content/category/<int:pk>/', MainContentCategoryView.as_view()),

]