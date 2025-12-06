from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "article_update.html"
    fields = ["title", "summary", "body", "photo"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("articles")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser


class ArticleCreateview(UserPassesTestMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ["title", "summary", "body", "photo"]
    login_url = "/login/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
