from .models import Category


def cats(request):
    return {
        'nav_cats': Category.objects.all()
    }