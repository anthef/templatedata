from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', dashboard, name='home'),
    path('link/add/', add_link, name='add_link'),
    path('link/<int:link_id>/edit/', edit_link, name='edit_link'),
    path('link/<int:link_id>/delete/', delete_link, name='delete_link'),
    path('category/add/', add_category, name='add_category'),
    path('category/<int:category_id>/edit/', edit_category, name='edit_category'),
    path('category/<int:category_id>/delete/', delete_category, name='delete_category'),
]