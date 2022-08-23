
from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet 

class CustomerAdmin(admin.ModelAdmin):
    list_display =("first_name","last_name","address","email","phonenumber","age")
    Search_Field=("first_name","last_name","Adress","email","age","phonenumber")
admin.site.register(Customer,CustomerAdmin)
class WalletAdmin(admin.ModelAdmin):
    list_display =("customer","currency","isActive","balance")
    Search_Field=("customer","currency","isActive","balance")
admin.site.register(Wallet,WalletAdmin)
class ReceiptAdmin(admin.ModelAdmin):
    list_display =("receiptdate","number","file","receipttype","amount")
    Search_Field=("receiptdate","number","file","receipttype","amount")
admin.site.register(Receipt,ReceiptAdmin)
class AccountAdmin(admin.ModelAdmin):
    list_display =("account_number","account_type","password","name")
    Search_Field=("account_number","account_type","password","name")
admin.site.register(Account,AccountAdmin)
class LoanAdmin(admin.ModelAdmin):
    list_display =("loan_number","amount","dateandtime","loanbalance","loanterm","payduedate","customer")
    Search_Field=("loan_number","amount","dateandtime","loanbalance","loanterm","payduedate","customer")  
admin.site.register(Loan,LoanAdmin)
class RewardAdmin(admin.ModelAdmin):
    list_display =("transaction","gender","date_and_time","points",)
    Search_Field=("transaction","gender","date_and_time","points",) 
admin.site.register(Reward,RewardAdmin)
class NotificationAdmin(admin.ModelAdmin):
    list_display =("name","date_and_time","status",)
    Search_Field=("name","date_and_time","status",) 
admin.site.register(Notification,NotificationAdmin)
class ThirdpartyAdmin(admin.ModelAdmin):
    list_display =("name","account","Phone_number","id",)
    Search_Field=("name","account","Phone_number","id",)
admin.site.register(Thirdparty,ThirdpartyAdmin)
class CardAdmin(admin.ModelAdmin):
    list_display =("card_number","user_name","card_type","Account",)
    Search_Field=("card_number","user_name","card_type","account")
admin.site.register(Card,CardAdmin)
class TransactionAdmin(admin.ModelAdmin):
    list_display =("transaction_code","transaction_amount","transaction_charge","destination_account")
    Search_Field=("transaction_code","transaction_amount","transaction_charge","destination_account")
admin.site.register(Transaction,TransactionAdmin)




# Register your models here.
