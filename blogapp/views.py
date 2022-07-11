from django.shortcuts import render, get_object_or_404
from flask import request
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# from django.urls.base import reverse_lazy
# from django.urls import reverse
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # print(posts[0].date_posted)
    return render(request,'blogapp/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'blogapp/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blogapp/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # success_url = reverse_lazy('blog-home')  
    # reverse() is used if urlconf is loaded
    #reverse_lazy() is used if urlconf is not loaded ie in classes 
    success_url = './'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def about(request):
    return render(request,'blogapp/about.html', {'title': 'About'})