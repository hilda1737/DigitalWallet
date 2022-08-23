from datetime import datetime
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(null=True,max_length=100)
    last_name = models.CharField(null=True,max_length=100)
    address = models.TextField(null=True,max_length=100)
    email = models.EmailField(null=True,max_length=150)
    phonenumber =models.CharField (max_length=16)
    age = models.IntegerField(null=True)


class Wallet(models.Model):  
   customer = models.ForeignKey(null=True,on_delete=models.CASCADE, to = Customer)
   currency = models.CharField(max_length=50,null=True)
   pin = models.PositiveSmallIntegerField()
   date_created = models.DateTimeField(default=datetime.now)
   isActive = models.BooleanField()
   balance = models.BigIntegerField(null=True)


class Receipt(models.Model):
    receiptdate=models.DateTimeField(default=datetime.now)
    number=models.IntegerField(null=True)
    file=models.FileField()
    receipttype=models.CharField(max_length=50,null=True)
    amount=models.BigIntegerField(null=True) 


class Account(models.Model):
    account_number=models.IntegerField(null=True)
    account_type=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=8,null=True)
    balance=models.IntegerField(null=True)
    name=models.CharField(max_length=15)

   

class Transaction(models.Model):
    transaction_code=models.CharField(max_length=8,null=True)
    transaction_amount=models.IntegerField(null=True)
    transaction_type=models.CharField(max_length=15,null=True)
    transaction_charge=models.IntegerField(null=True)
    transactiondateandtime=models.DateTimeField(default=datetime.now)
    receipt=models.OneToOneField(on_delete=models.CASCADE,to=Receipt)
    origin_account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name="account_a")
    destination_account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name="account_b")

class Card(models.Model):
    card_number=models.IntegerField(null=True)
    user_name=models.CharField(max_length=15,null=True)
    date_issue=models.DateTimeField(default=datetime.now)
    card_type=models.CharField(max_length=14,null=True)
    Account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)



class Thirdparty(models.Model):
    name=models.CharField(max_length=15,null=True)
    account=models.ForeignKey(on_delete=models.CASCADE,to=Account,null=True)
    Phone_number=models.CharField(max_length=15,null=True)
    id=models.PositiveSmallIntegerField(primary_key=True)


class Notification(models.Model):
    id_notification=models.PositiveSmallIntegerField(primary_key=True)
    name=models.CharField(max_length=15,null=True)
    date_and_time=models.DateTimeField(default=datetime.now)
    status=models.CharField(max_length=6)
   
class Loan(models.Model):
    loan_number=models.IntegerField(null=True)
    amount=models.BigIntegerField(null=True)
    dateandtime=models.DateTimeField(default=datetime.now)
    loanbalance=models.IntegerField(null=True)
    loanterm=models.IntegerField(null=True)
    payduedate=models.DateTimeField(default=datetime.now)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)

class Reward(models.Model):
    transaction=models.ForeignKey(on_delete=models.CASCADE,to=Transaction)
    customer_id=models.IntegerField(null=True)
    gender=models.CharField(max_length=6,null=True)
    date_and_time=models.DateTimeField(default=datetime.now)
    points=models.IntegerField(null=True)   






