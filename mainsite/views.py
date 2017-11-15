from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.utils import timezone

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
		'fade_in': True,
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
	if request.method == 'POST':
		form = ContactMessageForm(request.POST)
		if form.is_valid():
			new_message = ContactMessage()
			new_message.nom = form.cleaned_data['nom']
			new_message.contenu = form.cleaned_data['contenu']
			new_message.remote_addr = request.META['REMOTE_ADDR']
			new_message.timestamp = timezone.now()
			# # basic spam/double POST checker
			# existing_message = ContactMessage.objects.filter()
			new_message.save()
			messages.success(request, 'Votre message a bien été envoyé.')
		else:
			messages.error(request, 'Une erreur est survenue. Veuillez nous \
				contacter par un autre moyen.')
	else:
		pass
	context = {
		'contact_form' : ContactMessageForm(),
	}
	template = loader.get_template('mainsite/contact.html')
	return HttpResponse(template.render(context, request))

###############################################################################
def Privacy(request):
	'''
		Politique de confidentialité
	'''
	context = {
	}
	template = loader.get_template('mainsite/privacy.html')
	return HttpResponse(template.render(context, request))

###############################################################################
def Terms(request):
	'''
		Termes et conditions
	'''
	context = {
	}
	template = loader.get_template('mainsite/cgu.html')
	return HttpResponse(template.render(context, request))

###############################################################################
def BlogIndex(request):
	'''
		Blog main page
	'''
	# Fetch all the posts
	post_list = PostBlog.objects.all(
		).order_by('epingle', 'timestamp').reverse()
	# fetch all the tags
	tag_list = BlogTag.objects.all().order_by('nom')
	paginator = Paginator(post_list, 5)
	# Paginate them
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)

	context = {
		'posts' : posts,
		'tag_list' : tag_list,
	}
	template = loader.get_template('mainsite/blog_index.html')
	return HttpResponse(template.render(context, request))

#####################################################################
def BlogTagIndex(request, tag_uid):
	'''
		To view the blog posts
	'''
	current_state_data = CurrentStateCheck(request.user.id)
	all_tags = BlogTag.objects.all().order_by('name')
	tag = BlogTag.objects.get(pk = tag_uid)
	all_posts = list(PostBlog.objects.filter(tags__uid = tag.uid))
	for post in all_posts:
		post.content = post.content.split('</p>')[0]
	last_posts = all_posts[-5:]
	page_specifics = {
		'page_title': 'Vaste :: Blog',
		'tag': tag,
		'all_tags': all_tags,
		'all_posts': all_posts,
		'last_posts': last_posts,
	}
	context = {**current_state_data, **page_specifics}
	template = loader.get_template(
	'mainsite/blog_tag_index.html')
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
