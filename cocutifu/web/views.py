# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from web.models import Post, PostType


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(active=True)
        repertoires = PostType.objects.filter(name__icontains='Repertorio')
        if repertoires.exists():
        	context['repertoires'] = Post.objects.filter(types=repertoires[0])
        return context


class PostView(TemplateView):
    template_name = 'post.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, self.template_name, {'post': post})