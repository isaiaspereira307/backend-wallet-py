from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, BankAccount, Loan, Investment, FixedExpense, Bitcoin
from .serializers import TransactionSerializer, BankAccountSerializer, LoanSerializer, InvestmentSerializer, FixedExpenseSerializer, BitcoinSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['bank_account', 'timestamp']
    ordering_fields = ['amount', 'credit_debit', 'timestamp']

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['user', 'balance']
    ordering_fields = ['balance', 'name']


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['bank_account', 'due_date']
    ordering_fields = ['amount', 'due_date']

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['bank_account', 'created_at']
    ordering_fields = ['amount', 'created_at']

class FixedExpenseViewSet(viewsets.ModelViewSet):
    queryset = FixedExpense.objects.all()
    serializer_class = FixedExpenseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['bank_account', 'due_date']
    ordering_fields = ['amount', 'due_date']

class BitcoinViewSet(viewsets.ModelViewSet):
    queryset = Bitcoin.objects.all()
    serializer_class = BitcoinSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['bank_account', 'purchase_date']
    ordering_fields = ['quantity', 'purchase_date']

