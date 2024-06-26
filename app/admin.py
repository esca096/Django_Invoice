from django.contrib import admin
from .models import Customer, Invoice, Article
# Register your models here.

class AdminCustomer(admin.ModelAdmin):
    list_display = ('name','email','phone','address','city','created_date','save_by')
    
class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer','save_by','invoice_date','total','last_update_date','paid','invoice_type')
    
admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Article)
