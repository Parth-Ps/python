# from django.contrib.auth.models import User
import django_filters
from .models import	Product
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['price', 'categories', ]