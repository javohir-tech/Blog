from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView
)

urlpatterns = [
    path('' , ArticleListView.as_view() , name='articles'),
    path('detail/<int:pk>/' , ArticleDetailView.as_view() , name='article_detail'),
    path('detail/<int:pk>' , ArticleUpdateView.as_view() , name='article_update'),
]