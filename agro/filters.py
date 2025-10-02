# filters.py
import django_filters
from .models import AgricultureImplement

class AgricultureImplementFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    subcategory = django_filters.CharFilter(field_name='subcategory__name', lookup_expr='icontains')
    is_available = django_filters.BooleanFilter()
    isPopular = django_filters.BooleanFilter()
    isBestSeller = django_filters.BooleanFilter()
    implement_type = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = AgricultureImplement
        fields = ['category', 'subcategory', 'is_available', 'isPopular', 'isBestSeller', 'implement_type']
