from django.urls import path
from contact.views import contact_views


urlpatterns = [
    path('', contact_views.index, name='index'),
]
