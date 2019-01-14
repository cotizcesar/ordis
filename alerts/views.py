import requests
import json

# Django: Generic CBV
from django.views.generic import View, TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

class Alerts(TemplateView):
    template_name = 'alerts.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Alerts, self).get_context_data(**kwargs)
        r = requests.get('http://content.warframe.com/dynamic/worldState.php').json()
        r = json.dumps(r)
        r = r.replace('$', '')
        r = r.replace('_id', 'id')
        r = json.loads(r)
        context['alerts'] = r
        return context