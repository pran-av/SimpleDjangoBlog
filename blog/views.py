from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
# Create your views here.

class BlogListView(generic.ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(generic.CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(generic.UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']           #author not changing

class BlogDeleteView(generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
