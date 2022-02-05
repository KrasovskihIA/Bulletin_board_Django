from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from .forms_auth import *
from django.urls import reverse
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DetailView, UpdateView
from .models import Profile

class Login(LoginView):
    template_name = 'my_auth/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('index'), request)
        print(form.cleaned_data)
        return render(request, self.template_name, context={'form': form})


@login_required
def logout_views(request):
    logout(request)
    return redirect(reverse('index'))


class SignupViews(View):
    template_name = 'my_auth/signup.html'
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form':self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        registered = False
        context = {}
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data['email']
            user.save()
            registered = True
        else:
            context.update({'form':form})
        context.update({'registered':registered})
        return render(request, self.template_name, context=context)


class ProfileView(DetailView):
    model = Profile
    template_name = 'BulletinBoard/profile.html'

    def get_object(self):
        return get_object_or_404(self.model, user__id=self.kwargs['user_id'])


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'BulletinBoard/update_profile.html'

    slug_field = 'user_id'
    slug_url_kwarg = 'user_id'


    def dispatch(self, request, *args, **kwargs):
        obj=self.get_object()
        if obj.user != self.request.user:
            raise Http404('It not your profile')
        return super(UpdateProfileView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        user_id = self.kwargs['user_id']
        return reverse('profile', args=(user_id, ))