from .models import Category, Post
from django.db.models import Count
from marketing.forms import EmailForm


def cats(request):
    return {
        'nav_cats': Category.objects.all(),
        'pop_posts': Post.objects.annotate(num=Count('comments')).order_by('-num')[:6],
        'email_form': EmailForm()
    }
