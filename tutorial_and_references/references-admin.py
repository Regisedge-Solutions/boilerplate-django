# Inline forms - might have to use save_related here

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from .models import *

class CustomerAdmin(ImportExportModelAdmin):
    # ListView options 
    search_fields = ['name','email','phone','featured','created_on','updated_on']
    list_filter = ['featured','created_on','updated_on']
    list_per_page = 100
    list_display = ['id','name','email','phone','featured','created_on','updated_on']
    list_editable = ['featured']

    # DetailView options
    autocomplete_fields = ['tags']
    # filter_horizontal = ['village_pratinidhi','promoters']
    prepopulated_fields = {'slug': ('name',),}
    fieldsets = (
        (None, {
            'fields' : (
                ('name'),
                ('phone','email'),
                ('featured'),
                'tags',
            )
        }),
        ('Description', {
            'classes': ('collapse closed',), 
            'fields' : (
                'description',
            )
        }),
    )

admin.site.register(Customer, CustomerAdmin)