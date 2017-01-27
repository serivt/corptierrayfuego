# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from web.models import Post, PostType


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if 'type' in self.request.GET and self.request.GET['type']:
            post_type = get_object_or_404(PostType, pk=self.request.GET['type'])
            context['posts'] = Post.objects.filter(types=post_type, active=True)
        else:
            post_type, created = PostType.objects.get_or_create(name='Eventos')
            context['posts'] = Post.objects.filter(active=True, types=post_type).order_by('-pk')
        repertoires = PostType.objects.filter(name__icontains='Repertorio')
        if repertoires.exists():
        	context['repertoires'] = Post.objects.filter(types=repertoires[0])
        return context


class PostView(TemplateView):
    template_name = 'post.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, self.template_name, {'post': post})