from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
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