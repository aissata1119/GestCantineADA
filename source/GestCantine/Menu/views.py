from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Menu

# Vue pour lister les menus
class MenuListView(ListView):
    model = Menu
    template_name = 'menu/menu_list.html'  # Le fichier HTML à utiliser
    context_object_name = 'menus'  # Le nom sous lequel les objets seront passés dans le contexte

# Vue pour afficher les détails d'un menu
class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu/menu_detail.html'  # Le fichier HTML à utiliser

# Vue pour créer un nouveau menu
class MenuCreateView(CreateView):
    model = Menu
    template_name = 'menu/menu_form.html'  # Le fichier HTML à utiliser
    fields = ['creation_date']  # Les champs du formulaire à afficher

