# from dataclasses import fields
from django import forms
from .models import  Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"

class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model=Receipt
        fields="__all__"       


class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Card
        fields="__all__" 

class ThirdpartRegistration(forms.ModelForm):
    class Meta:
        model=Thirdparty
        fields="__all__"         

class NotificationRegistration(forms.ModelForm):
    class Meta:
        model=Notification
        fields="__all__" 

class NotificationReward(forms.ModelForm):
    class Meta:
        model=Reward
        fields="__all__" 

class NotificationLoan(forms.ModelForm):
    class Meta:
        model=Loan
        fields="__all__" 

class NotificationAccount(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__" 