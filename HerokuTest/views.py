from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse
from HerokuTest.models import Knight

class IndexView(ListView):
    template_name = 'upload.html'

    def get_queryset(self):
        list = []
        knights = Knight.objects.all()
        for k in knights:
            list.append(k.name)
        print list
        return list

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class CView(CreateView):
    model = Knight

    def get_success_url(self):
        return reverse('index')

