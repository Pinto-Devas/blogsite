from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Listagem de posts
class PostListView(ListView):
  model = Post
  template_name = 'blog/post_list.html'
  context_object_name = 'posts'
  ordering = ['-created_at']

# Detalhes de um post
class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post_detail.html'
  context_object_name = 'post'

# Criar um novo post
class PostCreateView(CreateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'blog/post_form.html'
  success_url = reverse_lazy('post_list')

# Editar um post existente
class PostUpdateView(UpdateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'blog/post_form.html'
  success_url = reverse_lazy('post_list')

# Deletar um post
class PostDeleteView(DeleteView):
  model = Post
  template_name = 'blog/post_confirm_delete.html'
  success_url = reverse_lazy('post_list')
