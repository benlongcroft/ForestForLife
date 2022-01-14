from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        extra_context = {'title': 'ForestForLife'}
        return extra_context



class ExplorePage(TemplateView):
    template_name = 'explore.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class SonnygamePage(LoginRequiredMixin, TemplateView):
    template_name = 'sonnygame.html'


class DataPolPage(TemplateView):
    template_name = 'datapolicy.html'


class PrivacyPolPage(TemplateView):
    template_name = 'privacypolicy.html'


class TnCPage(TemplateView):
    template_name = 'tnc.html'



