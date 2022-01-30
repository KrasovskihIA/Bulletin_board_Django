from msilib.schema import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from .models import *
from .forms import PostForm


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
    template_name = 'BulletinBoard/post_create.html'
    context = {'form': PostForm()}

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            context['post_was_created'] = True      
        else:
            context['post_with_errors'] = True
            context['form'] = form
    return render(request, template_name, context)

        




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
