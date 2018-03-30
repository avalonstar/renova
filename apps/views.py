from django.views.generic import TemplateView


class SiteView(TemplateView):
    template_name = 'landings/site_home.html'
