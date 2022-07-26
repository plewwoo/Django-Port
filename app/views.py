from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def index(request):

	return render(request, 'index.html')

def work(request, work):
	data = Work.objects.filter(siteCategory = work).order_by('id')

	context = {
		'data' : data,
	}

	return render(request, 'site/site.html', context)

def viewWork(request, work, id):
	work = Work.objects.get(id=id)
	image = Image.objects.filter(site = id)

	context = {
		'work' : work,
		'image' : image,
	}

	return render(request, 'site/viewSite.html', context)

def resume(request):
	return render(request, 'resume/resume.html')

@login_required(login_url="/login")
def add(request):

	categories = Work.objects.all()

	if request.method == 'POST':
		data = request.POST.copy()
		name = data.get('name')
		category = data.get('category')
		description = data.get('description')
		github = data.get('github')
		externalLink = data.get('externalLink')
		youtube = data.get('youtube')
		thumbnail = request.FILES['thumbnail']
		images = request.FILES.getlist('images')
		
		newWork = Work()
		newWork.siteName = name
		newWork.siteDesc = description
		newWork.github = github
		newWork.externalLink = externalLink
		newWork.siteCategory = category
		newWork.thumbnail = thumbnail
		x = youtube.split('=')
		y = x[1].split('&')
		newWork.youtube = y[0]
		newWork.save()

		for image in images:
			newImg = Image()
			newImg.site = Work.objects.get(siteName = name)
			newImg.image = image
			newImg.save()
			
		return redirect('home')
	
	context = {'categories': categories}
	return render(request, 'add/add.html', context)
