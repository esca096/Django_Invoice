from django.urls import path
from .views import AddInvoiceView, HomeView, AddCustomerView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-customer', AddCustomerView.as_view(), name='add-customer'),
    path('add-invoice', AddInvoiceView.as_view(), name='add-invoice'),
]
