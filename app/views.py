import imp
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def index(request):
	website = Work.objects.filter(siteCategory = 'website')
	paginator = Paginator(website, 3)
	websiteData = paginator.get_page(paginator)

	graphic = Work.objects.filter(siteCategory = 'graphic')
	paginator = Paginator(graphic, 3)
	graphicData = paginator.get_page(paginator)

	photograph = Work.objects.filter(siteCategory = 'photography')
	paginator = Paginator(photograph, 3)
	photographData = paginator.get_page(paginator)

	context = {
		'websiteData' : websiteData,
		'graphicData' : graphicData,
		'photographData' : photographData,
	}

	return render(request, 'index.html', context)

def site(request, site):
	data = Work.objects.filter(siteCategory = site)

	context = {
		'data' : data,
	}

	return render(request, 'site/site.html', context)

def viewSite(request, site, id):
	site = Work.objects.get(id=id)
	image = Image.objects.filter(site = id)

	context = {
		'site' : site,
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
		thumbnail = request.FILES['thumbnail']
		description = data.get('description')
		images = request.FILES.getlist('images')
		
		newSite = Work()
		newSite.siteName = name
		newSite.siteDesc = description
		newSite.siteCategory = category
		newSite.thumbnail = thumbnail
		newSite.save()

		for image in images:
			newImg = Image()
			newImg.site = Work.objects.get(siteName = name)
			newImg.image = image
			newImg.save()
			
		return redirect('home')
	
	context = {'categories': categories}
	return render(request, 'add/add.html', context)
