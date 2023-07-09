from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=255)


class Row(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='rows')
    data = models.JSONField()
