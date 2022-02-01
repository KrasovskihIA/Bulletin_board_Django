from django.core.exceptions import PermissionDenied
from ast import Delete
from audioop import reverse
from msilib.schema import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.base import View
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import *
from .forms import PostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class IndexView(ListView):
    model = Post
    template_name = 'BulletinBoard/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return self.model.objects.filter(date_pub__lte=timezone.now()).order_by('-date_pub')[:16]


class PostDeleteView(DeleteView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'BulletinBoard/post_delete.html'

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse('post_delete_success', args=(post_id, ))


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request,'BulletinBoard/post_detail.html', {'post':post})



class PostEditView(UpdateView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'BulletinBoard/post_edit.html'
    form_class = PostForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            raise PermissionDenied('Вы не автор этого объявления')
        else:
            return super(PostEditView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        post_id = self.kwargs[self.pk_url_kwarg]
        return reverse('post_detail', args=(post_id, ))



class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'BulletinBoard/post_create.html'

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            context['post_was_created'] = True  
            context['form'] = self.form_class 
        else:
            context['post_with_errors'] = True
            context['form'] = form
        return render(request, self.template_name, context)


class PostLikeView(View):
    def get(self, request, post_id, *args, **kwargs):
        return redirect(reverse('post', args=(post_id, )))
    
    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            post.save()
        return redirect(request.META.get('HTTP_REFERER'), request)
        
