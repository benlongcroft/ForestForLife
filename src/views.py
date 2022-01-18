"""
Forest For Life Views

Links all of the template views to classes
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def page_not_foundPage(request, exception):
    return render(request, '404.html', status=404)


class HomePage(TemplateView):
    template_name = 'index.html'


class ExplorePage(TemplateView):
    template_name = 'explore.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


# Requires user to be logged in in order to view
class SonnygamePage(LoginRequiredMixin, TemplateView):
    template_name = 'sonnygame.html'


class DataPolPage(TemplateView):
    template_name = 'datapolicy.html'


class PrivacyPolPage(TemplateView):
    template_name = 'privacypolicy.html'


class TnCPage(TemplateView):
    template_name = 'tnc.html'



