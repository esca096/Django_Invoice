from django.contrib import admin
from .models import Customer, Invoice, Article
from django.utils.translation import gettext_lazy as _
# Register your models here.

class AdminCustomer(admin.ModelAdmin):
    list_display = ('name','email','phone','address','city','created_date','save_by')
    
class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer','save_by','invoice_date','total','last_update_date','paid','invoice_type')
    
admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Article)

admin.site.site_title = _("SDI Invoice System")
admin.site.site_header = _("SDI Invoice System")
admin.site.index_title = _("SDI Administration")

