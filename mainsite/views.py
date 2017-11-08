from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

###############################################################################
def Home(request):
	'''
		Landing page for the main site. 
	'''
	context = {
	}
	template = loader.get_template('mainsite/home.html')
	return HttpResponse(template.render(context, request))