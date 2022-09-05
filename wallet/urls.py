# from unicodedata import name
from django.urls import path
from .views import   register_account, register_card, register_customers, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet
#urlspatters[stores urls ]
urlpatterns =[

    path("register/",register_customers,name="registration"),
    path("wallet/",register_wallet,name="wallet"),
    path("receipt/",register_receipt,name="receipt"),
    path("transaction/",register_transaction,name="transaction"),
    path("card/",register_card,name="card"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("Notification/",register_notification,name="notification"),
    path("Reward/",register_reward,name="reward"),
    path("Loan/",register_loan,name="loan"),
    path("account/",register_account,name="account"),







]