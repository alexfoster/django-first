# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
#from django.template import Context, loader
#from django.http.response import ( Http404, HttpResponse)
from django.shortcuts import (get_object_or_404, render)

from .models import Startup, Tag

# Create your views here.

def tag_list(request):
	return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

def tag_detail(request, slug):
	tag = get_object_or_404(Tag, slug__iexact=slug)
	return render(request, 'organizer/tag_list.html', {'tag': tag})	

def startup_list(request):
	return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})

def startup_detail(request, slug):
	startup = get_object_or_404(Startup, slug__iexact=slug)
	return render(request, 'organizer/startup_detail.html', {'startup': startup})
