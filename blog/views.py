from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.views import View
from django.conf import settings
from .models import Blog
from django.contrib import messages

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/home.html'


class CreateBlog(LoginRequiredMixin, TemplateView):
    template_name = 'blog/newBlog.html'
    def get(self,request):
        form = forms.BlogForm()
        return render(request,'blog/newBlog.html',{'form': form})

    def post(self,request):
        messages = ''
        form = forms.BlogForm()
        if request.method == 'POST':
            form = forms.BlogForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages = f'Blog is successFully created!'
                return redirect('/listBlog')
        return render(request,'blog/newBlog.html',{'form': form ,'message': message})

class BlogListing(LoginRequiredMixin, TemplateView):
    template_name = 'blog/blogListing.html'

    def get(self,request):
        blogs = Blog.objects.all()
        return render(request,self.template_name,{'blogs':blogs})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some_data'] = 'Hello, world!'
        return context
