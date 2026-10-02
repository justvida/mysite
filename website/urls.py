
from django.urls import path
from website.views import index_view, contact_view, about_view

urlpatterns = [
    path('', index_view),
    path('about', about_view),
    path('contact', contact_view)
]