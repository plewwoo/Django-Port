from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='home'),
	path('<str:work>/', work, name='work'),
	path('<str:work>/<int:id>', viewWork, name='viewWork'),
	path('add', add, name='add'),
	path('resume', resume, name='resume'),
]
