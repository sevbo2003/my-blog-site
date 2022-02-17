from django.shortcuts import render, get_object_or_404
from .models import Category, Author, Tags, Post, Comment
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from datetime import datetime


def index(request):
    key = request.GET.get('search')
    if key:
        posts = Post.objects.filter(Q(title__icontains=key) | Q(category__category__icontains=key))
    else:
        posts = Post.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    top_posts = Post.objects.filter(top=True)[:3]
    context = {
        'posts': posts,
        'top_posts': top_posts,
    }
    return render(request, 'index.html', context)


def uz_lang_posts(request):
    key = request.GET.get('search')
    if key:
        posts = Post.objects.filter(Q(title__icontains=key) | Q(category__category__icontains=key)).filter(
            language__exact='uz')
    else:
        posts = Post.objects.filter(language__exact='uz')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    top_posts = Post.objects.filter(top=True)[:3]
    context = {
        'posts': posts,
        'top_posts': top_posts,
    }
    return render(request, 'uzb_lang_posts.html', context)


def cat_posts(request, id, category):
    cat = get_object_or_404(Category, id=id, category=category)
    posts = Post.objects.filter(category=cat)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'cat': cat,
        'posts': posts
    }
    return render(request, 'category.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    try:
        post1 = Post.objects.get(id=post.id - 1)
    except:
        post1 = post
    try:
        post2 = Post.objects.get(id=post.id + 1)
    except:
        post2 = post
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            name = comment_form.cleaned_data['name']
            email = comment_form.cleaned_data['email']
            message = comment_form.cleaned_data['message']
            p = Comment(
                name=name,
                email=email,
                message=message,
                post=post,
                created_at=datetime
            )
            p.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'post1': post1,
        'post2': post2,
        'comment_form': comment_form
    }
    return render(request, 'post_detail.html', context)
