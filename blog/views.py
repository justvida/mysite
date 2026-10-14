from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if kwargs.get('cat_name') != None:
      posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!= None:
      posts = posts. filter(author__username = kwargs['author_username'])

    posts = Paginator(posts,3)
    try:
        page_number = request. GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    now = timezone.now()

    post = get_object_or_404(Post, id=pid, status=1, published_date__lte=now)

    post.counted_views += 1
    post.save()


    posts_list = list(Post.objects.filter(status=1, published_date__lte=now))

    current_index = posts_list.index(post)

    previous_post = posts_list[current_index - 1] if current_index > 0 else None

    next_post = posts_list[current_index + 1] if current_index < len(posts_list) - 1 else None

    context = {
        'post': post,
        'posts': posts_list,
        'previous_post': previous_post,
        'next_post': next_post,
    }

    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())

    if s := request.GET.get('s'):
        posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
