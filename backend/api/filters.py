from django_filters import rest_framework as filters
from django_filters.filters import BooleanFilter, ChoiceFilter, NumberFilter, OrderingFilter
from .models import Vacancy


class VacancyFilter(filters.FilterSet):
    experience = NumberFilter(field_name='experience')
    type_employment = NumberFilter(field_name='type_employment')
    work_schedule = NumberFilter(field_name='work_schedule')
    education = NumberFilter(field_name='education')
    remote_work = BooleanFilter(field_name='remote_work')
    sort = OrderingFilter(
        fields=(
            ('id', 'id'),
            ('salary','salary'),
        )
    )

    class Meta:
        model = Vacancy
        fields = ['experience', 'type_employment', 'work_schedule',
                   'education', 'remote_work']