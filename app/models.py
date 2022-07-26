from distutils.command.upload import upload
import site
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Work (models.Model):
	siteName = models.CharField(max_length=100, null=True, blank=True)
	siteDesc = models.TextField()
	siteCategory = models.CharField(max_length=100, choices=[('website', 'Website'), ('graphic', 'Graphic'), ('photography', 'Photography')])
	thumbnail = models.ImageField(upload_to='website_thumbnail/')
	externalLink = models.CharField(max_length=100, null=True, blank=True)
	github = models.CharField(max_length=100, null=True, blank=True)
	youtube = models.CharField(max_length=100, null=True, blank=True)
	createDate = models.DateTimeField(auto_now_add=True)
	updateDate = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Work'
		verbose_name_plural = 'Works'

	def __str__(self):
		return self.siteName

class Image(models.Model):
	site = models.ForeignKey(Work, on_delete=models.CASCADE, null=True, blank=True)
	image = models.ImageField(upload_to='image_website/', null=True, blank=True)

	def __str__(self):
		return self.site.siteName