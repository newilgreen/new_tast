from django_filters import rest_framework as filter
from subdivisions.models import Subdivision
from workers.models import Worker

class CharFilterInFilter(filter.BaseInFilter, filter.CharFilter):
    pass


class SubdivisionFilter(filter.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    abbreviation = CharFilterInFilter(field_name='abbreviation', lookup_expr='in')

    class Meta:
        model = Subdivision
        fields = ['name', 'abbreviation']

class SubworkerFilter(filter.FilterSet):
    subdivision = CharFilterInFilter(field_name='subdivision', lookup_expr='in')

    class Meta:
        model = Worker
        fields = ['subdivision']
