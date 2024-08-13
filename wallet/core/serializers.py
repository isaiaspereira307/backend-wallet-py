from rest_framework import serializers
from .models import Transaction, BankAccount, Loan, Investment, FixedExpense, Bitcoin
from .crypto_utils import get_bitcoin_price


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = "__all__"


class FixedExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedExpense
        fields = "__all__"


class BitcoinSerializer(serializers.ModelSerializer):
    current_btc_price = serializers.SerializerMethodField()

    class Meta:
        model = Bitcoin
        fields = ['bank_account', 'purchase_price', 'quantity', 'purchase_date', 'current_btc_price']

    def get_current_btc_price(self, obj):
        return get_bitcoin_price('USD')


