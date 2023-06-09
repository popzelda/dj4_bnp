import django_filters
from .models import Proprety

class PropretyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Proprety
        fields = ['price', 'name','category','place']