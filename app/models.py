from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Customer(models.Model):
    """
    Name: Customer model definition
    """
    
    SEX_TYPES = (
        ('M', _('Male')),
        ('F', _('Feminine')),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=132)
    address = models.CharField(max_length=64)
    sex = models.CharField(max_length=1, choices=SEX_TYPES)
    age = models.CharField(max_length=12)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=16)
    created_date= models.DateTimeField(auto_now=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        
    def __str__(self):
        return self.name


class Invoice(models.Model):
    """
    Name: Invoice model definition
    description:
    author: josuekoudahenou@gmail.com
    """
    
    INVOICE_TYPE = (
        ('R', _('RECEIPT')),
        ('P', _('PROFORMA INVOICE')),
        ('I', _('INVOICE')),
    )
    
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    invoice_date = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=1000000, decimal_places=3)
    last_update_date = models.DateTimeField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)
    commets = models.TextField(null=True, max_length=1000, blank=True)
    
    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
    
    
    def __str__(self):
        return f"{self.customer.name}_{self.invoice_date}"
    
    
    @property
    def get_total(self):
        articles = self.article_set.all()
        total = sum(article.get_total for article in articles)
        return total
    
class Article(models.Model):
    """
    Name: Article model definition
    description:
    author: josuekoudahenou@gmail.com
    """
    
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=1000, decimal_places=3)
    total = models.DecimalField(max_digits=10000, decimal_places=3)
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    
    def __str__(self):
        return self.name
        
    @property
    def get_total(self):
        total = self.quantity * self.unit_price
        return total