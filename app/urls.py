from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='home'),
	path('<str:site>/', site, name='site'),
	path('<str:site>/<int:id>', viewSite, name='viewSite'),
	path('add', add, name='add'),
	path('resume', resume, name='resume'),
]
