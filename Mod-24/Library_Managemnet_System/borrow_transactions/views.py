from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect,render
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from borrow_transactions.constants import DEPOSIT
from datetime import datetime
from django.db.models import Sum
from borrow_transactions.forms import (DepositForm, BorrowBookForm)
from borrow_transactions.models import BorrowTransaction
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = BorrowTransaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount 
        account.save(
            update_fields=['balance']
                    )
        messages.success(
            self.request, f'{"{:,.2f}".format(float(amount))} BDT was deposited to your account successfully'
                        )
        send_transaction_email(self.request.user, amount, "Deposite Message", "transactions/deposite_email.html")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.req,"User has no Account!")
        return redirect("no_account")
    


class BorrowBookFormView(TransactionCreateMixin):
    form_class = BorrowBookForm
    title = 'Borrow Book'

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')

        self.request.user.account.balance -= form.cleaned_data.get('amount')
        self.request.user.account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )

        return super().form_valid(form)


class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = BorrowTransaction
    balance = 0 
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            
            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = BorrowTransaction.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance
       
        return queryset.distinct() 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })

        return context
    
def no_account(req):
    return render (req,'transactions/no_account.html')
    
        