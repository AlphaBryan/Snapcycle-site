from django.contrib import admin
from django.urls import path
# from snapcycle.views import accueil, contact, mission, propos, beta, thanks
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('propos/', views.propos, name="propos"),
    path('beta/', views.beta, name="beta"),
    path('thanks/', views.thanks, name="thanks"),
    path('contact/', views.contact, name="contact"),
    path('mission/', views.mission, name="mission"),

]