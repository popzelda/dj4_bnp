from django.shortcuts import render, reverse
from django.views.generic import ListView,DetailView
from .models import *

class PropretyList(ListView):
    model = Proprety
    paginate_by = 1
    ### filter
    ### paginatuin
class PropretyDetail(DetailView):
    model = Proprety
    ### book
