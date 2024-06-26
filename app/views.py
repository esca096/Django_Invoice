from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages

from django.db import transaction
from .utils import paginator


# Create your views here.

class HomeView(View):
    """ Main View """
    
    template_name = 'index.html'
    invoices = Invoice.objects.select_related('customer', 'save_by').all()
    
    context = {
        'invoices':invoices
    }
    
    def get(self, request, *args, **kwargs):
        
        #permet la pargination depuis utils
        items = paginator(request, self.invoices)
        self.context['invoices'] = items
        
        return render(request, self.template_name, self.context)
    
    
    def post(self, request, *args, **kwargs):
        
        #Modification an invoice
        
        if request.POST.get('id_modified'):
            paid = request.POST.get('modified')
            
            try:
                obj = Invoice.objects.get(id=request.POST.get('id_modified'))
                if paid == 'True':
                    obj.paid = True
                else:
                    obj.paid = False
                obj.save()
                messages.success(request, "change made successfully")
                
            except Exception as e:
                messages.error(request, f"Sorry the following error has occured {e}.")
                
        #Deleting an invoice
        
        if request.POST.get('id_supprimer'):
            
            try:
                obj = Invoice.objects.get(pk=request.POST.get('id_supprimer'))
                
                obj.delete()
                
                messages.success(request, 'the deletion was successfully')
            
            except Exception as e:
                messages.error(request, f"Sorry the following error has occured {e}.")
        
        #permet la pargination depuis utils
        items = paginator(request, self.invoices)
        self.context['invoices'] = items  
        
        
        return render(request, self.template_name, self.context)
    
    
class AddCustomerView(View):
    """ Add new Customer"""
    
    template_name = 'add_customer.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        
        data = {
            'name':request.POST.get('name'),
            'email':request.POST.get('email'),
            'phone':request.POST.get('phone'),
            'sex':request.POST.get('sex'),
            'age':request.POST.get('age'),
            'address':request.POST.get('address'),
            'city':request.POST.get('city'),
            'zip_code':request.POST.get('zip'),
            'save_by':request.user
        }
        
        try:
            created = Customer.objects.create(**data)
            
            if created:
                messages.success(request, "Customer registered successfully")
                
            else:
                messages.error(request, "Sorry, Please try again!!! the sent data ")
                
        except Exception as e:
            
            messages.error(request, f"Sorry our system is detecting the following issues {e} ")
        
        return render(request, self.template_name)
    
    
class AddInvoiceView(View):
    """ add a new invoice view"""
        
    template_name = 'add_invoice.html'
        
    customers = Customer.objects.select_related('save_by').all()
        
    context ={
        'customers':customers
    }
        
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,  self.context)
    
    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        items = []
        
        try:
            customer = request.POST.get('customer')
            type = request.POST.get('invoice_type')
            articles = request.POST.getlist('article')
            qties = request.POST.getlist('qty')
            units = request.POST.getlist('unit')
            total_a = request.POST.getlist('total-a')
            total = request.POST.get('total') 
            comment = request.POST.get('comments')
            
            invoice_object ={
                'customer_id': customer,
                'save_by': request.user,
                'total': total,
                'invoice_type': type,
                #'comments': comment,
            }
            
            invoice = Invoice.objects.create(**invoice_object)
            
            for index, article in enumerate(articles):
                
                data = Article(
                    invoice_id = invoice.id,
                    name = article,
                    quantity = qties[index],
                    unit_price = units[index],
                    total = total_a[index],
                )
                
                items.append(data)
            
            created = Article.objects.bulk_create(items)
            
            if created:
                messages.success(request, "Data save successfully")
            else:
                messages.error(request, "Sorry!!!, try again")
                
        except Exception as e:
            messages.error(request, f"Sorry the following error has occured {e}.")
        return render(request, self.template_name,  self.context)
        