from django.db import models
from django.utils import timezone

#####################################################################
class BlogTag(models.Model):
    '''
        Posts on the blog
    '''
    # Attributes
    uid = models.AutoField(
        primary_key = True, db_index = True)
    name = models.CharField(
        max_length = 50)
    # Methods
    def __str__(self):
        return str(self.name)

#####################################################################
class PostBlog(models.Model):
    '''
        Posts on the blog
    '''
    # Attributes
    uid = models.AutoField(
        primary_key = True, db_index = True)
    name = models.CharField(
        max_length = 50)
    content = models.TextField(
        )
    tags = models.ManyToManyField(
        BlogTag, related_name = 'postblog_blogtag')
    timestamp =  models.DateTimeField(
        default = timezone.now)
    # Methods
    def __str__(self):
        return str(self.name)

###############################################################################
class OrchideeGenre(models.Model):
	'''
	'''
	# Attributes
	uid = models.AutoField(
		primary_key= True, db_index= True)
	genre = models.CharField(
		max_length = 255)
	img = models.ImageField(
		upload_to='static/mainsite/img/orchidee/',
		default= 'static/mainsite/img/orchidee/orchidee_default.png',
		help_text = "Essayer de recadrer l'image pour qu'elle soit le plus \
		carrée possible. Si pas d'image fournie, une image par défaut est prévue.")
	# Methods
	def __str__(self):
		return self.genre

###############################################################################
class Orchidee(models.Model):
	'''
		Table des orchidées
	'''
	# Attributes
	uid = models.AutoField(
		primary_key= True, db_index= True)
	genre = models.ForeignKey(
		OrchideeGenre, related_name = 'orchidee_orchideegenre')
	espece = models.CharField(
		max_length= 255)
	description = models.TextField(
		)
	img = models.ImageField(
		upload_to='static/mainsite/img/orchidee/',
		default= 'static/mainsite/img/orchidee/orchidee_default.png',
		help_text = "Essayer de recadrer l'image pour qu'elle soit le plus \
		carrée possible. Si pas d'image fournie, une image par défaut est prévue.")
	prix = models.DecimalField(
		max_digits = 6, decimal_places = 2,
		help_text = "Il faut spécifier les deux décimales pour les centimes \
		même si le prix est rond. Veuillez entrer ,00 à la fin dans ce cas. \
		Par exemple, 27€ --> 27,00 et 27,90€ --> 27.90")
	mis_en_avant = models.BooleanField(
		default = False,
		help_text = "Cocher cette case si vous voulez mettre cet article \
		en avant sur la page d'accueil du site.")
	discount = models.PositiveIntegerField(
		null = True, blank = True,
		help_text = "Laisser vide si l'article n'est pas soldé. \
		Si cet article est en soldes, entrer le pourcentage de \
		la solde. Il sera automatiquement mis en avant sur la page \
		d'accueil avec la valeur de la solde et le prix soldé, pas besoin \
		de cocher la valeur 'mise en avant'.")
	# Methods
	def __str__(self):
		return str("{} {}".format(self.genre, self.espece))

###############################################################################
class PlanteGenre(models.Model):
	'''
	'''
	# Attributes
	uid = models.AutoField(
		primary_key= True, db_index= True)
	genre = models.CharField(
		max_length = 255)
	img = models.ImageField(
		upload_to='static/mainsite/img/plante/',
		default= 'static/mainsite/img/plante/plante_default.png',
		help_text = "Essayer de recadrer l'image pour qu'elle soit le plus \
		carrée possible. Si pas d'image fournie, une image par défaut est prévue.")
	# Methods
	def __str__(self):
		return self.genre

###############################################################################
class Plante(models.Model):
	'''
		Table des plantes hors orchidées
	'''
	# Attributes
	uid = models.AutoField(
		primary_key= True, db_index= True)
	genre = models.ForeignKey(
		PlanteGenre, related_name = 'plante_plantegenre')
	espece = models.CharField(
		max_length= 255)
	description = models.TextField(
		)
	img = models.ImageField(
		upload_to='static/mainsite/img/plante/',
		default= 'static/mainsite/img/plante/plante_default.png',
		help_text = "Essayer de recadrer l'image pour qu'elle soit le plus \
		carrée possible. Si pas d'image fournie, une image par défaut est prévue.")
	prix = models.DecimalField(
		max_digits = 6, decimal_places = 2,
		help_text = "Il faut spécifier les deux décimales pour les centimes \
		même si le prix est rond. Veuillez entrer ,00 à la fin dans ce cas. \
		Par exemple, 27€ --> 27,00 et 27,90€ --> 27,90")
	mis_en_avant = models.BooleanField(
		default = False,
		help_text = "Cocher cette case si vous voulez mettre cet article \
		en avant sur la page d'accueil du site.")
	discount = models.PositiveIntegerField(
		null = True, blank = True,
		help_text = "Laisser vide si l'article n'est pas soldé. \
		Si cet article est en soldes, entrer le pourcentage de \
		la solde. Il sera automatiquement mis en avant sur la page \
		d'accueil avec la valeur de la solde et le prix soldé, pas besoin \
		de cocher la valeur 'mise en avant'.")
	# Methods
	def __str__(self):
		return str("{} {}".format(self.genre, self.espece))

###############################################################################
class Pot(models.Model):
	'''
		Table des pots et poteries
	'''
	# Attributes
	uid = models.AutoField(
		primary_key= True, db_index= True)
	nom = models.CharField(
		max_length= 255)
	description = models.TextField(
		)
	img = models.ImageField(
		upload_to='static/mainsite/img/pot/',
		default= 'static/mainsite/img/pot/pot_default.png',
		help_text = "Essayer de recadrer l'image pour qu'elle soit le plus \
		carrée possible. Si pas d'image fournie, une image par défaut est prévue.")
	prix = models.DecimalField(
		max_digits = 6, decimal_places = 2,
		help_text = "Il faut spécifier les deux décimales pour les centimes \
		même si le prix est rond. Veuillez entrer ,00 à la fin dans ce cas. \
		Par exemple, 27€ --> 27,00 et 27,90€ --> 27.90")
	mis_en_avant = models.BooleanField(
		default = False,
		help_text = "Cocher cette case si vous voulez mettre cet article \
		en avant sur la page d'accueil du site.")
	discount = models.PositiveIntegerField(
		null = True, blank = True,
		help_text = "Laisser vide si l'article n'est pas soldé. \
		Si cet article est en soldes, entrer le pourcentage de \
		la solde. Il sera automatiquement mis en avant sur la page \
		d'accueil avec la valeur de la solde et le prix soldé, pas besoin \
		de cocher la valeur 'mise en avant'.")
	# Methods
	def __str__(self):
		return str(self.nom)

###############################################################################
class Materiel(models.Model):
	'''
		Table du petit matériel
	'''
	# Attributes
	uid = models.AutoField(
		primary_key= True, db_index= True)
	nom = models.CharField(
		max_length= 255)
	description = models.TextField(
		)
	img = models.ImageField(
		upload_to='static/mainsite/img/materiel/',
		default= 'static/mainsite/img/materiel/materiel_default.png',
		help_text = "Essayer de recadrer l'image pour qu'elle soit le plus \
		carrée possible. Si pas d'image fournie, une image par défaut est prévue.")
	prix = models.DecimalField(
		max_digits = 6, decimal_places = 2,
		help_text = "Il faut spécifier les deux décimales pour les centimes \
		même si le prix est rond. Veuillez entrer ,00 à la fin dans ce cas. \
		Par exemple, 27€ --> 27,00 et 27,90€ --> 27.90")
	mis_en_avant = models.BooleanField(
		default = False,
		help_text = "Cocher cette case si vous voulez mettre cet article \
		en avant sur la page d'accueil du site.")
	discount = models.PositiveIntegerField(
		null = True, blank = True,
		help_text = "Laisser vide si l'article n'est pas soldé. \
		Si cet article est en soldes, entrer le pourcentage de \
		la solde. Il sera automatiquement mis en avant sur la page \
		d'accueil avec la valeur de la solde et le prix soldé, pas besoin \
		de cocher la valeur 'mise en avant'.")
	# Methods
	def __str__(self):
		return str(self.nom)