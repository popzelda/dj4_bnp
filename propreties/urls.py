from django.urls import path
from .views import *
app_name = 'propreties'

urlpatterns = [
    path('list/', PropretyList.as_view(),name='prop_list'),
    path('detail/<slug:slug>', PropretyDetail.as_view(),name='prop_detail'),


]