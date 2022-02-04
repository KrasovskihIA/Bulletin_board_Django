from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils import timezone
from django.db.models.fields import DateTimeField



# Класс профиля
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    birth_data = models.DateField('Дата регистрации', blank=False, auto_now_add=True, null=False)
    about = models.TextField(max_length=1000, blank=True)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return f'{self.user.username}'



# Класс категорий
class Category(models.Model):
    name = models.CharField('Категория', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Класс обьявлений
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    title = models.TextField(max_length=100, blank=False)
    description = models.TextField('Описание', max_length=1000, blank=False)
    image = models.ImageField(upload_to='posts/')
    date_pub = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='Категория', blank=False, on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='users_likes_it')
    contact = models.CharField(max_length=15)
    

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'



# Класс комментариев
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    text = models.TextField(max_length=500)
    in_post = models.ForeignKey(Post, on_delete=CASCADE)
    date_publish = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'

