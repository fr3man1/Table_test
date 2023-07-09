import logging
from django.db import models

logger = logging.getLogger(__name__)


class Table(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Row(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='rows')
    data = models.JSONField()

    def __str__(self):
        return f"Row {self.pk} of Table {self.table_id}"

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error occurred while saving Row {self.pk}: {str(e)}")
            raise
