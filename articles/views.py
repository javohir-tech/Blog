from django.shortcuts import render
from .models import Article
from django.views.generic import ListView , DetailView


class ArticleListView(ListView) :
    model = Article;
    template_name = 'article_list.html'

# Create your views here.
