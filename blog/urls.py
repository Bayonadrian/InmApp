from django.urls import path

# Views
from .views import BlogView, PostView

urlpatterns= [
    path('', BlogView.as_view(), name='blog_main'),
    path('posts/<int:pk>', PostView.as_view(), name= 'blog_posts')
]