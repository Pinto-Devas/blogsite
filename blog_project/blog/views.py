from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post

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
    title = request.POST.get('title')
    content = request.POST.get('content')
    if title and content:  # Validação simples
      Post.objects.create(title=title, content=content)
      return HttpResponseRedirect('/')
  return render(request, 'blog/post_form.html')

# Editar um post existente
def post_update(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
    title = request.POST.get('title')
    content = request.POST.get('content')
    if title and content:
      post.title = title
      post.content = content
      post.save()
      return HttpResponseRedirect(f'/posts/{post.pk}/')
  return render(request, 'blog/post_form.html', {'post': post})

# Deletar um post
def post_delete(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
    post.delete()
    return HttpResponseRedirect('/')
  return render(request, 'blog/post_confirm_delete.html', {'post': post})
