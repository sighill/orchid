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
class AdminPot(admin.ModelAdmin):
    list_display= ['uid', 'nom', 'prix', 'mis_en_avant', 'discount']
    ordering= ['nom']
admin.site.register(Pot, AdminPot)

###############################################################################
class AdminMateriel(admin.ModelAdmin):
    list_display= ['uid', 'nom', 'prix', 'mis_en_avant', 'discount']
    ordering= ['nom']
admin.site.register(Materiel, AdminMateriel)

#####################################################################
class AdminBlogTag(admin.ModelAdmin):
    list_display= ['uid', 'name']
    ordering= ['uid']
admin.site.register(BlogTag, AdminBlogTag)

#####################################################################
class AdminPostBlog(admin.ModelAdmin):
    list_display= ['uid','name']
    ordering= ['uid']
admin.site.register(PostBlog, AdminPostBlog)


'''
###############################################################################
class Admin(admin.ModelAdmin):
    list_display= ['uid',]
    ordering= ['uid']
admin.site.register(, Admin)
'''