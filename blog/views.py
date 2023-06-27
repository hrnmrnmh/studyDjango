from django.shortcuts import render
from blog.models import Post


def post_list(request):
    context = {"posts": Post.objects.all()}
    return render(request, 'blog/post_list.html', context)
