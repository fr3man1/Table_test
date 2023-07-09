from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Table, Row

class TableBuilderAPITestCase(TestCase):
    table = None

    def setUp(self):
        self.client = APIClient()

    def test_create_table(self):
        url = reverse('table-list-create')
        data = {'name': 'MyTable'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Table.objects.count(), 1)
        self.assertEqual(Table.objects.get().name, 'MyTable')

    def test_update_table(self):
        table = Table.objects.create(name='OldName')
        url = reverse('table-retrieve-update', kwargs={'id': table.id})
        data = {'name': 'NewName'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Table.objects.get().name, 'NewName')

    def test_add_row(self):
        table = Table.objects.create(name='MyTable')
        url = reverse('row-create', kwargs={'id': table.id})
        data = {'table':Table.objects.get().id,'data': {'column1': 'value1', 'column2': 'value2'}}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Row.objects.count(), 1)
        self.assertEqual(Row.objects.get().table, table)

    def test_get_rows(self):
        table = Table.objects.create(name='MyTable')
        Row.objects.create(table=table, data={'column1': 'value1', 'column2': 'value2'})
        Row.objects.create(table=table, data={'column1': 'value3', 'column2': 'value4'})
        url = reverse('row-list', kwargs={'id': table.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
