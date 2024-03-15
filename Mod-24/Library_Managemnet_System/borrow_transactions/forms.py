from django import forms
from .models import BorrowTransaction
from book.models import BookModel
from django.shortcuts import get_object_or_404


class BorrowTransactionForm(forms.ModelForm):
    class Meta:
        model = BorrowTransaction
        fields = ['amount' , 'transaction_type']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_borrow = self.account.balance
        return super().save()


class DepositForm(BorrowTransactionForm):
    def clean_amount(self): 
        min_deposit_amount = 250
        amount = self.cleaned_data.get('amount') 
        if amount < min_deposit_amount:
            raise forms.ValidationError
        (
            f'You need to deposit at least {min_deposit_amount} BDT'
        )
        return amount


class BorrowBookForm(BorrowTransactionForm):
    def clean_amount(self):
        account = self.account
        amount = self.cleaned_data.get('amount')
        book = get_object_or_404(BookModel, id=self.instance.book_id)

        if amount < book.borrowing_price:
            raise forms.ValidationError
            (
                f'You have not much balance in your Wallet'
            )
        return amount
