from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Contact page
    path('contact/', views.contact, name='contact'),

    # About page
    path('about/', views.about, name='about'),

    # Checkout page
    path('checkout/', views.checkout, name='checkout'),

    # Handler request endpoint
    path('handlerequest/', views.handlerequest, name='handlerequest'),

    # Profile page
    path('profile/', views.profile, name='profile'),
]
