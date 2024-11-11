from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm
from faker import Faker

def post_list(request):
    """
    View function for listing all blog posts.
    """
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    """
    View function for displaying a single blog post.
    """
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    """
    View function for creating a new blog post.
    """
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'post_form.html', {'form': form, 'action': 'Create'})

def post_update(request, pk):
    """
    View function for updating an existing blog post.
    """
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'post_form.html', {'form': form, 'action': 'Update'})

def post_delete(request, pk):
    """
    View function for deleting a blog post.
    """
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog:post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})


def fake_post(request, total):
    fake= Faker() 

    for _ in range(total):
        BlogPost.objects.create(title=fake.sentence(), 
                            description=fake.text(), 
                            tags=f"{fake.word()},{fake.word()},{fake.word()}"
        )
        
        # Item.objects.create(title=fake.sentence(), description=fake.text(), price=fake.random_number(digits=2) )
    return redirect('item:item_list')