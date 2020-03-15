from django.contrib.admin import register, ModelAdmin
from django.contrib.admin.helpers import ActionForm
from django.db.models import QuerySet
from django.forms import IntegerField, ModelChoiceField
from django.http import HttpRequest

from case.models import Case
from user.models import City


class AddCaseActionForm(ActionForm):
    number_cases = IntegerField(required=False)
    city = ModelChoiceField(queryset=City.objects.all(), required=False)


@register(Case)
class CaseAdmin(ModelAdmin):
    list_display = (
        'city', 'patient', 'in_quarantine', 'is_tested_positive', 'is_hospitalized', 'is_dead', 'is_recovered',
        'symptoms_gravity', 'additional_details', 'created_at', 'updated_at'
    )
    fields = (
        'city', 'patient', 'in_quarantine', 'is_tested_positive', 'is_hospitalized', 'is_dead', 'is_recovered',
        'symptoms_gravity', 'additional_details'
    )
    ordering = ('-updated_at',)
    action_form = AddCaseActionForm
    actions = ('add_cases',)
    list_filter = (
        'automatically_created', 'city', 'in_quarantine', 'is_tested_positive', 'is_hospitalized', 'is_dead',
        'is_recovered'
    )

    def add_cases(self, request: HttpRequest, _: QuerySet):
        print(request.POST['city'])
        number_cases = int(request.POST['number_cases'])
        city = City.objects.get(uuid=request.POST['city'])
        cases_to_create = [
            Case(additional_details=f'This case is created automatically by admin for {city.name}', in_quarantine=False,
                 automatically_created=True, city=city)
            for _ in range(number_cases)
        ]
        Case.objects.bulk_create(cases_to_create)
