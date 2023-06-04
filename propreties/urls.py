from django.urls import path
from .views import *
app_name = 'propreties'

urlpatterns = [
    path('list/', PropretyList.as_view()),
    path('detail/', PropretyDetail.as_view()),


]