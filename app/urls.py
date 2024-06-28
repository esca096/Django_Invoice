from django.urls import path
from .views import AddInvoiceView, HomeView, AddCustomerView, InvoiceVisualizationView, get_invoice_pdf
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-customer', AddCustomerView.as_view(), name='add-customer'),
    path('add-invoice', AddInvoiceView.as_view(), name='add-invoice'),
    path('view-invoice/<int:pk>', InvoiceVisualizationView.as_view(), name='view-invoice'),
    path('invoice-pdf/<int:pk>', get_invoice_pdf, name='invoice-pdf'),
]
