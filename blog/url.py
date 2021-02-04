from django.urls import path
from .views import PostListView, PostDetailListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailListView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]