from django.urls import path
from .views import MenuListView, MenuDetailView, MenuCreateView, MenuUpdateView, MenuDeleteView

urlpatterns = [
    path('', MenuListView.as_view(), name='menu_list'),  # URL pour la liste des menus
    path('<str:pk>/', MenuDetailView.as_view(), name='menu_detail'),  # URL pour les détails d'un menu
    path('create/', MenuCreateView.as_view(), name='menu_create'),  # URL pour créer un menu
    path('<str:pk>/update/', MenuUpdateView.as_view(), name='menu_update'),  # URL pour mettre à jour un menu
    path('<str:pk>/delete/', MenuDeleteView.as_view(), name='menu_delete'),  # URL pour supprimer un menu
]
