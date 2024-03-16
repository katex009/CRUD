from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView
from django.views.generic.edit import CreateView

# Create your views here.

class BlogListView(ListView):
    model = Publication
    template_name = 'home.html'

class BlogCreateView(CreateView):
    model = Publication
    template_name = 'post_new.html'
    fields = ['title', 'body', 'author']