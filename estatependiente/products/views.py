from django.shortcuts import render_to_response
from django.template.context import RequestContext

from .models import Category,Product
from estatependiente.parameters.models import Parameter

def view_category(request,category):
    categories = Category.objects.all()
    products = Product.objects.filter(category__path=category)
    subcategories = products.values('subcategory__name','subcategory__path').distinct()
    parameters = Parameter.objects.all()
    return render_to_response('products.html',
                            {'categories': categories,
                            'products': products,
                            'subcategories': subcategories,
                            'contact': parameters.get(name='contacto')
                            },context_instance=RequestContext(request))

def view_product(request,product):
    categories = Category.objects.all()
    pr = Product.objects.get(path=product)
    parameters = Parameter.objects.all()
    return render_to_response('product.html',
                            {'categories': categories,
                            'product': pr,
                            'contact': parameters.get(name='contacto')
                            },context_instance=RequestContext(request))

