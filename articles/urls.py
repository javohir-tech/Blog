from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateview,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("detail/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("create/", ArticleCreateview.as_view(), name="article_create"),
    path("detail/update/<int:pk>/", ArticleUpdateView.as_view(), name="article_update"),
    path("detail/delete/<int:pk>/", ArticleDeleteView.as_view(), name="article_delete"),
]
