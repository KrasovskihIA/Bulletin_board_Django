from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from .models import *


class IndexViews(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request,'posts/index.html', {'post_list':posts})