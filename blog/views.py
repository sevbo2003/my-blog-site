from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Author, Tags, Post, Comment
from django.db.models import Q, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from datetime import datetime
from django.http import HttpResponseRedirect
from marketing.forms import EmailForm, ContactForm
from marketing.models import Email
from django.core.mail import send_mail


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
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            print(email)
            p = Email(email=email)
            p.save()
    else:
        email_form = EmailForm()
    context = {
        'posts': posts,
        'top_posts': top_posts,
    }
    return render(request, 'index.html', context)
    Post.objects.filter(com)


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
            link = f"{post.get_absolute_url()}#comments"
            return HttpResponseRedirect(link)
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'post1': post1,
        'post2': post2,
        'comment_form': comment_form
    }
    return render(request, 'post_detail.html', context)


def contact_page(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            text = f"{message}\nfrom --> {name}"
            send_mail('malikov.co', text, 'sevbofx@gmail.com', (email,))
    else:
        contact_form = ContactForm()
    return render(request, 'page-contact.html', {'contact_form': contact_form})
