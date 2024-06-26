from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginator(request, invoices):
    # default page 
    default_page = 1
    page = request.GET.get('page', default_page)
        
    #parginate items
    items_per_page = 5
    paginator = Paginator(invoices, items_per_page)
        
    try:
        items_page = paginator.page(page)
            
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
            
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)
            
    return items_page