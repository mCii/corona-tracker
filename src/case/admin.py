from django.contrib.admin import register, ModelAdmin

from case.models import Case


@register(Case)
class CaseAdmin(ModelAdmin):
    list_display = (
        'location', 'patient', 'in_quarantine', 'is_tested_positive', 'is_hospitalized', 'is_dead', 'is_recovered',
        'symptoms_gravity', 'additional_details', 'created_at', 'updated_at'
    )
    fields = list_display
    ordering = ('-updated_at',)
