from django.shortcuts import render, redirect
from django.http import HttpResponse
from pages.models import Blog
from pages.forms import BlogForm

# Create your views here.
def home(request):
    posts = Blog.objects.all()
    return render(request, 'index.html', {'posts': posts})

def contact(request):
    return render(request, 'contact.html')

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Blog(title=title, content=content)
        if post is not None:
            post.save()
            return redirect('home')
    return render(request, 'create.html')

def delete(request, id):
    post = Blog.objects.get(id=id)
    post.delete()
    return redirect('home')

def update(request, id):
    post = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=post)
    return render(request, 'update.html', {'form': form})