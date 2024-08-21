from django.urls import path
from faject.category.views import CategoryView, SubCategoryView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('sub/category/', SubCategoryView.as_view()),

]