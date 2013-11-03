# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect

from estatependiente.products.models import Category,Product
from estatependiente.parameters.models import Parameter

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:3]
    parameters = Parameter.objects.all()
    welcome = parameters.get(name='bienvenida')
    contact = parameters.get(name='contacto')
    return render_to_response('home.html',
                            {'categories': categories,
                            'products': products,
                            'welcome': welcome,
                            'contact': contact,
                            },context_instance=RequestContext(request))

