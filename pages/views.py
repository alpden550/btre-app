from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'pages/index.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
