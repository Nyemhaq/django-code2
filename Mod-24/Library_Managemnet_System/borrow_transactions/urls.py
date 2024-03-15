from django.urls import path
from .views import DepositMoneyView, BorrowBookFormView, TransactionReportView,no_account

urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionReportView.as_view(), name="transaction_report"),
    path("withdraw/", BorrowBookFormView.as_view(), name="withdraw_money"),
    path("no_account/", no_account, name="no_account"),

]