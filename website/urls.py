

from django.urls import path
from . import views

urlpatterns = [

	path('', views.home, name="home"),
	path('our_story.html', views.our_story, name="our_story"),
	path('events.html', views.events, name="events"),
	path('gallery.html', views.gallery, name="gallery"),
	path('contact.html', views.contact, name="contact"),
	path('testimonials.html', views.testimonials, name="testimonials"),


 

]
