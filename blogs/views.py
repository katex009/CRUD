from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

class BlogListView(ListView):
    model = Publication
    template_name = 'home.html'

class BlogCreateView(CreateView):
    model = Publication
    template_name = 'post_new.html'
    fields = ['title', 'body', 'author']

class BlogDetailView(DetailView):
    model = Publication
    template_name = 'post_detail.html'

class BlogUpdateView(UpdateView):
    model = Publication
    template_name = 'post_edit.html'
    fields = ['title', 'body']