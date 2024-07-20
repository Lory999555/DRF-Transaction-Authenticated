from django.urls import path
from .views import TransactionListCreateView, TransactionDeleteView

urlpatterns = [
    path('', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction-delete'),
]
