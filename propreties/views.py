from django.shortcuts import render, reverse
from django.views.generic import ListView,DetailView
from .models import *

class PropretyList(ListView):
    model = Proprety
    paginate_by = 3
    ### filter
    ### paginatuin

class PropretyDetail(DetailView):
    model = Proprety
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Proprety.objects.filter(category=self.get_object().category)[:2]
        return context
    ### book





















































