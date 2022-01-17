"""ForestForLife URL Configuration

The 'urlpatterns' list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('profiles/', include('django.contrib.auth.urls')),
    path('support/', include('support.urls', namespace='support')),
    path('explore/', views.ExplorePage.as_view(), name='explore'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('sonnygame/', views.SonnygamePage.as_view(), name='sonnygame'),
    path('data_policy', views.DataPolPage.as_view(), name='data_policy'),
    path('privacy_policy', views.PrivacyPolPage.as_view(), name='privacy_policy'),
    path('terms_and_cond', views.TnCPage.as_view(), name='terms_and_cond')

]
