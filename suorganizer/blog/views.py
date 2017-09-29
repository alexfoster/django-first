# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import (get_object_or_404, render)
from django.views.generic import View

# Create your views here.

from .models import Post

class PostList(View):
	template_name = 'blog/post_list.html'

	def get(self, request):
		return render(request, self.template_name, {'post_list': Post.objects.all()})

def post_detail(request, year, month, slug):
	post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
	return render(request, 'blog/post_detail.html', {'post': post})
