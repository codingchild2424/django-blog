from django.shortcuts import render
from .models import Post

def index(request):

    posts = Post.objects.all().order_by('-pk') #이렇게 하면 pk값을 기준으로 역순으로 정렬

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )