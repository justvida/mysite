from django. shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.db.models import F


# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()
    ).order_by('-published_date')
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request):
    return render(request, 'blog/blog-single.html')


def increase_views(post):
    """Add 1 to counted_view of this post."""
    Post.objects.filter(pk=post.pk).update(counted_views=F('counted_views') + 1)


def blog_single(request):
    post_id = request.GET.get('id')          # ?id=1 in the address
    if post_id:
        post = Post.objects.filter(pk=post_id).first()
    else:
        post = Post.objects.first()          # no id: use the first post

    if post:
        increase_views(post)                 # +1 every time the page opens
        post.refresh_from_db()

    return render(request, 'blog/blog-single.html', {'post': post})



