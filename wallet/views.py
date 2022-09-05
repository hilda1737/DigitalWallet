from django.shortcuts import render
from  .forms import  CardRegistrationForm, CustomerRegistrationForm, NotificationAccount, NotificationLoan, NotificationRegistration, NotificationReward, ReceiptRegistrationForm, ThirdpartRegistration, TransactionRegistrationForm, WalletRegistrationForm



def register_customers(request):
 form=CustomerRegistrationForm()
 return render(request,"wallet/register_customers.html", {'form':form})

def register_wallet(request): 
  form=WalletRegistrationForm()
  return render(request,"wallet/wallet.html", {'form':form})

def register_receipt(request): 
  form=ReceiptRegistrationForm()
  return render(request,"receipt.html", {'form':form})


def register_transaction(request): 
  form=TransactionRegistrationForm()
  return render(request,"transaction.html", {'form':form})

def register_card(request): 
  form=CardRegistrationForm()
  return render(request,"card.html", {'form':form})

def register_thirdparty(request): 
  form=ThirdpartRegistration()
  return render(request,"thirdparty.html", {'form':form})


def register_notification(request): 
  form=NotificationRegistration()
  return render(request,"notification.html", {'form':form})

def register_reward(request): 
  form=NotificationReward()
  return render(request,"reward.html", {'form':form})

def register_loan(request): 
  form=NotificationLoan()
  return render(request,"loan.html", {'form':form})

def register_account(request): 
  form=NotificationAccount()
  return render(request,"account.html", {'form':form})


 
  #processes the request
 

#we handle http request
# Create your views here.
