from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *

class PropretyList(ListView):
    model = Proprety
### filter
class PropretyDetail(DetailView):
    pass
### book
