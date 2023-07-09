from django.urls import path
from tables.views import (
    TableListCreateAPIView,
    TableRetrieveUpdateAPIView,
    RowCreateAPIView,
    RowListAPIView,
)

urlpatterns = [
    path('api/table/', TableListCreateAPIView.as_view(), name='table-list-create'),
    path('api/table/<int:id>/', TableRetrieveUpdateAPIView.as_view(), name='table-retrieve-update'),
    path('api/table/<int:id>/row/', RowCreateAPIView.as_view(), name='row-create'),
    path('api/table/<int:id>/rows/', RowListAPIView.as_view(), name='row-list'),
]
