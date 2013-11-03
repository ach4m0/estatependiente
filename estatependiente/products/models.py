# -*- coding: utf-8 -*-

from django.db import models

class CommonFields(models.Model):
    """
    Clase abstracta con los campos comunes para los modelos de products
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField(editable=False,auto_now_add=True)
    update_date = models.DateTimeField(editable=False,auto_now=True)
    visible = models.BooleanField(default=True)
    path = models.CharField(max_length=100,unique=True)

    class Meta:
        abstract=True

class Catalog(CommonFields):
    """
    Modelo para permitir dar de alta diferentes catalogos.

    Hereda todos sus campos de CommonFields
    """
    def __unicode__(self):
        return self.name

class Category(CommonFields):
    """
    Modelo para referenciar las categorias de los productos
    """
    def __unicode__(self):
        return self.name

class Subcategory(CommonFields):
    """
    Modelo para referenciar las subcategorias de los productos
    """
    def __unicode__(self):
        return self.name

class Product(CommonFields):
    """
    Modelo para almacenar los productos de la tienda
    """
    available = models.BooleanField(default=True)
    image1 = models.FileField(upload_to='uploads',null=True,blank=True)
    image2 = models.FileField(upload_to='uploads',null=True,blank=True)
    image3 = models.FileField(upload_to='uploads',null=True,blank=True)
    ref_code = models.CharField(max_length=50,unique=True)
    stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    #Relationships
    category = models.ForeignKey(Category)
    subcategory = models.ForeignKey(Subcategory,null=True,blank=True)
    catalog = models.ForeignKey(Catalog)

    def __unicode__(self):
        return self.name
