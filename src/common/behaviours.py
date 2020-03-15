import logging

import uuid
from django.db import models
from django.db.models import Model, DateTimeField

logger = logging.getLogger(__name__)


class Timestampable(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(db_index=True, auto_now=True)

    class Meta:
        abstract = True


class UUIDable(models.Model):
    uuid = models.CharField(max_length=64, editable=False, primary_key=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = self.generate_uuid()
        super().save(*args, **kwargs)

    def generate_uuid(self):
        return str(uuid.uuid4()).upper()
