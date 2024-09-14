from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Post

class BlogView(ListView):

    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 4

    #def get_queryset(self):
        #return Post.objects.order_by('-date') # To sort popsts on negative date

class PostView(DetailView):

    model = Post
    template_name = 'posts.html'