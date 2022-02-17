from django.db import models
from ckeditor.fields import RichTextField


class Author(models.Model):
    full_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='author_img')
    bio = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Authors'
        verbose_name = 'author'

    def __str__(self):
        return self.full_name


class Category(models.Model):
    category = models.CharField(max_length=15)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'category'

    def __str__(self):
        return self.category


class Tags(models.Model):
    tag = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'Tags'
        verbose_name = 'tag'

    def __str__(self):
        return self.tag


class Post(models.Model):
    LANGUAGES = (
        ('uz', 'Uzbek'),
        ('eng', 'English')
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tags, related_name='tags')
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnail_posts')
    image = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    top = models.BooleanField(default=False)
    language = models.CharField(max_length=3, choices=LANGUAGES, default='eng')
    body = RichTextField()
    slug = models.SlugField()

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Posts'
        verbose_name = 'post'

    def __str__(self):
        return self.title + ' | ' + str(self.language)

    def get_absolute_url(self):
        return f"/post/{self.slug}/"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Comments'
        verbose_name = 'comment'

    def __str__(self):
        return self.name
