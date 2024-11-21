from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import CommentForm

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

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['comments'] = self.object.comments.order_by('-created_at')
    return context

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
  
class CommentCreateView(CreateView):
  model = Comment
  form_class = CommentForm
  template_name = "blog/comment_form.html"

  def form_valid(self, form):
    form.instance.author = self.request.user
    form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
    return super().form_valid(form)

  def get_success_url(self):
    return reverse('post_detail', kwargs={'pk': self.kwargs['pk']})

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
    return context
