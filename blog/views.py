from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
  context = {
    'posts' : Post.objects.all()
  }
  return render(request,'blog/home.html', context)

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html in this case app: blog , model :Post, viewtype: list
  context_object_name = 'posts' # to match the variable name between html and model
  ordering = ['-date_posted'] # - is desc 

class PostDetailListView(DetailView):
  model = Post
     

def about(request):
  return render(request,'blog/about.html', {'title':'About'} )
# Create your views here.
