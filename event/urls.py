from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, {'liked' : False}, name='home'),
	path('toggle/<int:pk>/<int:liked>', views.toggle, name='toggle'),
	path('create-event', views.create, name='create'),
	path('liked', views.home, {'liked' : True}, name='liked')
]