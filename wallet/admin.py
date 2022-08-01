
from ast import Load
from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet 




class CustomerAdmin(admin.ModelAdmin):
    list_display =("first_name","last_name","Adress","email","phonenumber","age")
    Search_Field=("first_name","last_name","Adress","email","age","phonenumber")
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Receipt)
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Notification)
admin.site.register(Thirdparty)
admin.site.register(Card)
admin.site.register(Transaction)




# Register your models here.
