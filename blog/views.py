from django.shortcuts import Http404, render, get_object_or_404, redirect
from blog.models import Post
from django.utils import timezone
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        return render(request, 'blog/post_detail.html', {'post': post})
    else:
        if (not post.published_date) or timezone.now() < post.published_date:
            raise Http404

    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if not request.user.is_authenticated:
        return redirect('/admin/')

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk: int):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_draft_list(request):
    if not request.user.is_authenticated:
        raise Http404
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, pk: int):
    if not request.user.is_authenticated:
        raise Http404
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=post.pk)


def post_remove(request, pk: int):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
