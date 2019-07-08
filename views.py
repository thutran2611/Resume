import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	index_html = open('content/index.html').read()
	context = {'content':index_html,}

	return render(request,'base.html',context)

def experience(request):
	experience_html = open('content/experience.html').read()
	context = {'content':experience_html
	'link':index()}
	return render(request,'base.html',context)

def blog(request):
	blog_html = open('content/blog.html').read()
	context = {'content':blog_html}
	return render(request,'base.html',context)
