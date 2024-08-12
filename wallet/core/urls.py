from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, BankAccountViewSet, LoanViewSet, InvestmentViewSet, FixedExpenseViewSet, BitcoinViewSet

# Crie um roteador
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'bankaccounts', BankAccountViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'investments', InvestmentViewSet)
router.register(r'fixedexpenses', FixedExpenseViewSet)
router.register(r'bitcoins', BitcoinViewSet)

# Inclua as URLs do roteador
urlpatterns = [
    path('', include(router.urls)),
]