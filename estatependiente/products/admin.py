# -*- coding: utf-8 -*-

from django.contrib import admin

from estatependiente.products import models

class CommonAdmin(admin.ModelAdmin):
    list_display = ('name','visible','update_date')
    search_fields = ('name','description')
    readonly_fields = ('create_date','update_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','visible','available','ref_code','catalog')
    search_fields = ('name','description','ref_code')
    readonly_fields = ('create_date','update_date')

#Models registered
admin.site.register(models.Catalog,CommonAdmin)
admin.site.register(models.Category,CommonAdmin)
admin.site.register(models.Subcategory,CommonAdmin)
admin.site.register(models.Product,ProductAdmin)
