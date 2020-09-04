from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def our_story(request):
	return render(request, 'our_story.html', {})


def events(request):
	return render(request, 'events.html', {})		

def gallery(request):
	return render(request, 'gallery.html', {})


def contact(request):
	return render(request, 'contact.html', {})

def testimonials(request):
	return render(request, 'testimonials.html', {})	