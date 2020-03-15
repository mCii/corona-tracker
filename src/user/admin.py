from django.contrib.admin import register, ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import User, City, Region, Nationality


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


@register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'uuid', 'email', 'first_name', 'last_name', 'is_staff', 'is_patient', 'identity_card_number', 'passport_number',
        'phone_number', 'age')
    list_filter = ('is_staff',)
    search_fields = ('first_name', 'last_name', 'email', 'identity_card_number', 'passport_number', 'phone_number')
    ordering = ('first_name', 'last_name')

    # Detail
    fieldsets = (
        (None, {'fields': ('email', 'password', 'created_at', 'updated_at')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'phone_number', 'identity_card_number', 'passport_number', 'nationality', 'age')}),
        ('Permissions', {'fields': ('is_staff', 'is_patient')}),
    )
    add_fieldsets = ((None, {'classes': ('wide',),
                             'fields': ('email', 'password1', 'password2', 'first_name', 'last_name'), }),)
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    readonly_fields = ('created_at', 'updated_at')


@register(City)
class CityAdmin(ModelAdmin):
    list_display = ('uuid', 'name',)
    fields = ('name',)
    readonly_fields = ('uuid',)


@register(Region)
class RegionAdmin(ModelAdmin):
    list_display = ('uuid', 'name', 'city',)
    fields = ('name', 'city',)
    readonly_fields = ('uuid',)


@register(Nationality)
class NationalityAdmin(ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
