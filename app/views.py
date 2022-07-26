import imp
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def index(request):

	return render(request, 'index.html')

def site(request, site):
	data = Work.objects.filter(siteCategory = site)

	context = {
		'data' : data,
	}

	return render(request, 'site/site.html', context)

def viewSite(request, site, id):
	work = Work.objects.get(id=id)
	image = Image.objects.filter(site = id)

	context = {
		'work' : work,
		'image' : image,
	}

	return render(request, 'site/viewSite.html', context)

def resume(request):
	return render(request, 'resume/resume.html')

def add(request):

	categories = Work.objects.all()

	if request.method == 'POST':
		data = request.POST.copy()
		name = data.get('name')
		category = data.get('category')
		description = data.get('description')
		github = data.get('github')
		externalLink = data.get('externalLink')
		thumbnail = request.FILES['thumbnail']
		images = request.FILES.getlist('images')
		
		newWork = Work()
		newWork.siteName = name
		newWork.siteDesc = description
		newWork.github = github
		newWork.externalLink = externalLink
		newWork.siteCategory = category
		newWork.thumbnail = thumbnail
		newWork.save()

		for image in images:
			newImg = Image()
			newImg.site = Work.objects.get(siteName = name)
			newImg.image = image
			newImg.save()
			
		return redirect('home')
	
	context = {'categories': categories}
	return render(request, 'add/add.html', context)
