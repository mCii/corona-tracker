import logging
import os
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

logger = logging.getLogger(__name__)


def get_image_path(_, filename):
    return os.path.join(settings.BASE_DIR, 'src', 'data', filename)


class Timestampable(models.Model):
    """
    With this behavior mixed in, an object gets two fields that are filled automatically on
    creation or update of the object.

    This class inherits from models.Model, since it adds fields to the Django model. Otherwise,
    these Django does not recognize these fields, e.g. if you want to use them for sorting.
    """

    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(db_index=True, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        now = timezone.now()

        if not self.created_at:
            self.created_at = now

        if not kwargs.pop('skip_updated_at', False):
            self.updated_at = now

        super().save(*args, **kwargs)


class UUIDable(models.Model):
    """
    With this behavior mixed in, an object gets a field that is automatically filled with a UUID string when an object
    is created

    This class inherits from models.Model, since it adds fields to the Django model. Otherwise,
    these Django does not recognize these fields, e.g. if you want to use them for sorting.
    """

    uuid = models.CharField(max_length=64, editable=False, primary_key=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = self.generate_uuid()
        super().save(*args, **kwargs)

    def generate_uuid(self):
        return str(uuid.uuid4()).upper()

# TODO: will get deleted
# def formfield_for_manytomany(self, db_field, request, **kwargs):
#     if db_field.name == 'extras':
#         product_id = request.resolver_match.kwargs.get('object_id')
#         if product_id:
#             product_id = product_id.replace('5F', '')
#             customer = Product.objects.get(uuid=product_id).customer
#             kwargs['queryset'] = Extra.objects.filter(customer=customer)
#     return super().formfield_for_manytomany(db_field, request, **kwargs)
