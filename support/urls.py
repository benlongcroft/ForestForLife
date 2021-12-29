from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('donate/', views.donate, name="donate"),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('d_success/', views.d_success, name='d_success'),
    path('d_cancelled/', views.d_cancelled, name='d_cancelled')
]