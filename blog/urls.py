from django.urls import path
from . import views as blog_views


urlpatterns = [
    path('', blog_views.index, name='home'),
    path('uz/', blog_views.uz_lang_posts, name='home_uz'),
    path('category/<str:category>/<int:id>/', blog_views.cat_posts, name='category')
]