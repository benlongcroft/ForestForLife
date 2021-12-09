from django.views.generic import TemplateView


class LoginTest(TemplateView):
    template_name = 'logintest.html'


class LogoutTest(TemplateView):
    template_name = 'logouttest.html'


class HomePage(TemplateView):
    template_name = 'index.html'


class ExplorePage(TemplateView):
    template_name = 'explore.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class SonnygamePage(TemplateView):
    template_name = 'sonnygame.html'

