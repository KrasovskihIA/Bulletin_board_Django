from msilib.schema import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from .models import *


class IndexViews(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request,'BulletinBoard/index.html', {'post_list':posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request,'BulletinBoard/post_detail.html', {'post':post})




def post_edit(request, post_id):
    return HttpResponse(f'Редактирование обьявления номер {post_id}')

def post_create(request):
    return HttpResponse(f'Создание нового обьявления')

def post_delete(request, post_id):
    return HttpResponse(f'Удаление обьявления номер {post_id}')

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        post.save()
    return redirect(request.META.get('HTTP_REFERER'), request)
