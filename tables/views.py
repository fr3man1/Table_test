from rest_framework import generics
from .models import Table, Row
from .serializers import TableSerializer, RowSerializer


class TableListCreateAPIView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_url_kwarg = 'id'


class RowCreateAPIView(generics.CreateAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer
    lookup_url_kwarg = 'id'

    def perform_create(self, serializer):
        table_id = self.kwargs.get('id')
        table = Table.objects.get(id=table_id)
        serializer.save(table=table)


class RowListAPIView(generics.ListAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        table_id = self.kwargs.get('id')
        return Row.objects.filter(table_id=table_id)
