from django.contrib import admin
from .models import *

###############################################################################
class AdminOrchideeGenre(admin.ModelAdmin):
    list_display= ['uid', 'genre',]
    ordering= ['genre']
admin.site.register(OrchideeGenre, AdminOrchideeGenre)

###############################################################################
class AdminOrchidee(admin.ModelAdmin):
    list_display= ['uid', 'genre', 'espece', 'prix', 'mis_en_avant', 'discount']
    ordering= ['genre']
admin.site.register(Orchidee, AdminOrchidee)

###############################################################################
class AdminPlanteGenre(admin.ModelAdmin):
    list_display= ['uid', 'genre',]
    ordering= ['genre']
admin.site.register(PlanteGenre, AdminPlanteGenre)

###############################################################################
class AdminPlante(admin.ModelAdmin):
    list_display= ['uid', 'genre', 'espece', 'prix', 'mis_en_avant', 'discount']
    ordering= ['genre']
admin.site.register(Plante, AdminPlante)

###############################################################################
class AdminPotCategory(admin.ModelAdmin):
    list_display= ['uid', 'categorie']
    ordering= ['categorie']
admin.site.register(PotCategory, AdminPotCategory)

###############################################################################
class AdminPot(admin.ModelAdmin):
    list_display= ['uid', 'nom', 'prix', 'mis_en_avant', 'discount']
    ordering= ['nom']
admin.site.register(Pot, AdminPot)

###############################################################################
class AdminMaterielCategory(admin.ModelAdmin):
    list_display= ['uid', 'categorie']
    ordering= ['categorie']
admin.site.register(MaterielCategory, AdminMaterielCategory)

###############################################################################
class AdminMateriel(admin.ModelAdmin):
    list_display= ['uid', 'nom', 'prix', 'mis_en_avant', 'discount']
    ordering= ['nom']
admin.site.register(Materiel, AdminMateriel)

#####################################################################
class AdminBlogTag(admin.ModelAdmin):
    list_display= ['uid', 'nom']
    ordering= ['uid']
admin.site.register(BlogTag, AdminBlogTag)

#####################################################################
class AdminPostBlog(admin.ModelAdmin):
    list_display= ['uid','titre']
    ordering= ['uid']
admin.site.register(PostBlog, AdminPostBlog)


'''
###############################################################################
class Admin(admin.ModelAdmin):
    list_display= ['uid',]
    ordering= ['uid']
admin.site.register(, Admin)
'''