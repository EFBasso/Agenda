from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    # contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
]

"""
PADRÃO URLS (exemplos que facilitam entender o que a url faz)
    # contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.contact, name='contact'),
    path('contact/<int:contact_id>/delete/', views.contact, name='contact'),

    # users (CRUD)
    path('user/<int:user_id>/detail/', views.user, name='user'),
    path('user/create/', views.user, name='user'),
    path('user/<int:user_id>/update/', views.user, name='user'),
    path('user/<int:user_id>/delete/', views.user, name='user'),
"""
