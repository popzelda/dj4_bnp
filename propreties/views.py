from django.shortcuts import render, reverse
from django.views.generic import ListView,DetailView
from .models import *
from django_filters.views import FilterView
from .filters import PropretyFilter

class PropretyList(FilterView):
    model = Proprety
    paginate_by = 3
    filterset_class = PropretyFilter
    template_name = 'propreties/proprety_list.html'
    ### filter
    ### paginatuin

class PropretyDetail(DetailView):
    model = Proprety
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Proprety.objects.filter(category=self.get_object().category)[:2]
        return context
    ### book





















































