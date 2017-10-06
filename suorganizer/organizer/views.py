# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
#from django.template import Context, loader
#from django.http.response import ( Http404, HttpResponse)
from django.shortcuts import (get_object_or_404, render, redirect)
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, View
from django.urls import reverse, reverse_lazy

from .models import NewsLink, Startup, Tag
from .forms import NewsLinkForm, StartupForm, TagForm

# Create your views here.


class TagList(View):
    template_name = 'organizer/tag_list.html'

    def get(self, request):
        tags = Tag.objects.all()
        context = {
            'tag_list': tags,
        }
        return render(
            request, self.template_name, context)

class TagDetail(DetailView):
	model = Tag

class TagCreate(CreateView):
	form_class = TagForm
	model = Tag

class TagUpdate(UpdateView):
	form_class = TagForm
	model = Tag
	template_name = ('organizer/tag_form_update.html')

class TagDelete(DeleteView):
	model = Tag
	success_url = reverse_lazy('organizer_tag_list')

def startup_list(request):
	return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})

class StartupDetail(DetailView):
	model = Startup

class StartupCreate(CreateView):
	form_class = StartupForm
	model = Startup

class StartupUpdate(UpdateView):
	form_class = StartupForm
	model = Startup
	template_name = ('organizer/startup_form_update.html')

class StartupDelete(DeleteView):
	model = Startup
	success_url = reverse_lazy('organizer_startup_list')

class NewsLinkCreate(CreateView):
	form_class = NewsLinkForm
	model = NewsLink

class NewsLinkUpdate(View):
	form_class = NewsLinkForm
	template_name = ('organizer/newslink_form_update.html')

	def get(self, request, pk):
		newslink = get_object_or_404(NewsLink, pk=pk)
		context = {'form': self.form_class(instance=newslink),}
		return render(request, self.template_name, context)

	def post(self, request, pk):
		newslink = get_object_or_404(NewsLink, pk=pk)
		bound_form = self.form_class(request.POST, instance=newslink)
		if bound_form.is_valid():
			new_newslink = bound_form.save()
			return redirect(new_newslink)
		else:
			context = {'form': bound_form, 'newslink': newslink,}
			return render(request, self.template_name, context)

class NewsLinkDelete(View):

	def get(self, request, pk):
		newslink = get_object_or_404(NewsLink, pk=pk)
		return render(request, 'organizer/newslink_form_delete.html', {'newslink': newslink})

	def post(self, request, pk):
		newslink = get_object_or_404(NewsLink, pk=pk)
		startup = newslink.startup
		newslink.delete()
		return redirect(startup)
