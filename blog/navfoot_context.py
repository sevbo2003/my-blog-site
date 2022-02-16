from .models import Category, Post


def cats(request):
    return {
        'nav_cats': Category.objects.all(),
        'pop_posts': Post.objects.all()[:6]
    }