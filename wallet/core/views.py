from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, BankAccount, Loan, Investment, FixedExpense, Bitcoin
from .serializers import TransactionSerializer, BankAccountSerializer, LoanSerializer, InvestmentSerializer, FixedExpenseSerializer, BitcoinSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    pagination_class = [IsAuthenticated]

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class FixedExpenseViewSet(viewsets.ModelViewSet):
    queryset = FixedExpense.objects.all()
    serializer_class = FixedExpenseSerializer

class BitcoinViewSet(viewsets.ModelViewSet):
    queryset = Bitcoin.objects.all()
    serializer_class = BitcoinSerializer

