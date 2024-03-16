from django.urls import path
from .views import BlogListView, BlogCreateView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
]