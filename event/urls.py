from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('toggle/<int:pk>', views.toggle, name='toggle'),
	path('create-event', views.create, name='create'),
	path('liked', views.liked, name='liked')
]