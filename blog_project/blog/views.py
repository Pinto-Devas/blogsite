from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Listagem de posts
def post_list(request):
  posts = Post.objects.all().order_by('-created_at')
  return render(request, 'blog/post_list.html', {'posts': posts})

# Detalhes de um post
def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {'post': post})

# Criar um novo post
def post_create(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('post_list')
  else:
    form = PostForm()
  return render(request, 'blog/post_form.html', {'form': form})

# Editar um post existente
def post_update(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm(instance=post)
  return render(request, 'blog/post_form.html', {'form': form})

# Deletar um post
def post_delete(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
    post.delete()
    return redirect('post_list')
  return render(request, 'blog/post_confirm_delete.html', {'post': post})
