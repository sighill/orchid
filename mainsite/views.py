from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import *

###############################################################################
def Home(request):
	'''
		Landing page for the main site. 
	'''
	highlighted_orchidees = Orchidee.objects.filter(mis_en_avant = True)
	discount_orchidees = Orchidee.objects.exclude(discount = None)
	highlighted_plants = Plante.objects.filter(mis_en_avant = True)
	discount_plants = Plante.objects.exclude(discount = None)
	highlighted_pots = Pot.objects.filter(mis_en_avant = True)
	discount_pots = Pot.objects.exclude(discount = None)
	highlighted_materiels = Materiel.objects.filter(mis_en_avant = True)
	discount_materiels = Materiel.objects.exclude(discount = None)

	home_vegetals = Orchidee.objects.none()
	home_vegetals = home_vegetals.union(
		highlighted_orchidees, discount_orchidees, highlighted_plants, 
		discount_plants)
	home_objects = Pot.objects.none()
	home_objects = home_objects.union(
		highlighted_pots, discount_pots, highlighted_materiels, 
		discount_materiels)
	context = {
		'home_vegetals' : home_vegetals,
		'home_objects' : home_objects,
	}
	template = loader.get_template('mainsite/home.html')
	return HttpResponse(template.render(context, request))

###############################################################################
def OrchideeIndex(request, chosen_genre = None):
    '''
    	Displays an index of orchid items available.
    '''
    # Récupérer les objets permettant de faire les catégories filtrables
    all_orchidee_genres = OrchideeGenre.objects.all().order_by('genre')
    # Essayer de récupérer le genre choisi par l'utilisateur
    chosen_genre = str(request.GET.get('genre'))
    # Si la variable genre a été spécifiée, on récupère les 
    if chosen_genre:
        items_to_display = Orchidee.objects.filter(genre__genre = chosen_genre)
    else:
        items_to_display = None
    context = {
        'scroll_down_on_load' : True,
    	'all_orchidee_genres' : all_orchidee_genres,
    	'items_to_display' : items_to_display,
        'chosen_genre' : chosen_genre,
    }
    template = loader.get_template('mainsite/orchidee_index.html')
    return HttpResponse(template.render(context, request))

###############################################################################
def PlanteIndex(request, chosen_genre = None):
    '''
        Displays an index of plant items available.
    '''
    # Récupérer les objets permettant de faire les catégories filtrables
    all_plante_genres = PlanteGenre.objects.all().order_by('genre')
    # Essayer de récupérer le genre choisi par l'utilisateur
    chosen_genre = str(request.GET.get('genre'))
    # Si la variable genre a été spécifiée, on récupère les 
    if chosen_genre:
        items_to_display = Plante.objects.filter(genre__genre = chosen_genre)
    else:
        items_to_display = None
    context = {
        'scroll_down_on_load' : True,
        'all_plante_genres' : all_plante_genres,
        'items_to_display' : items_to_display,
        'chosen_genre' : chosen_genre,
    }
    template = loader.get_template('mainsite/plante_index.html')
    return HttpResponse(template.render(context, request))

###############################################################################
def HardwareIndex(request, hardware_category):
    '''
        Displays an index of hardware (pot or tools) items available.
    '''
    if hardware_category == Pot:
        jumbotron_title = 'Tous nos pots'
    else:
        jumbotron_title = 'Tout notre petit matériel'
    # Essayer de récupérer le genre choisi par l'utilisateur
    hardware_to_display = hardware_category.objects.all().order_by('nom')
    context = {
        'hardware_to_display' : hardware_to_display,
        'jumbotron_title' : jumbotron_title,
    }
    template = loader.get_template('mainsite/hardware_index.html')
    return HttpResponse(template.render(context, request))

###############################################################################
def Contact(request):
    '''
        Simple contact view
    '''
    context = {
    }
    template = loader.get_template('mainsite/contact.html')
    return HttpResponse(template.render(context, request))

###############################################################################
def Privacy(request):
    '''
        Simple contact view
    '''
    context = {
    }
    template = loader.get_template('mainsite/privacy.html')
    return HttpResponse(template.render(context, request))    

"""
###############################################################################
def (request):
    '''
    '''
    context = {
    }
    template = loader.get_template('.html')
    return HttpResponse(template.render(context, request))
"""
