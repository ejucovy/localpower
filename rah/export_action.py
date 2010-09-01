import csv

from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.contrib import admin

def admin_list_export(modeladmin, request, queryset):
    model = queryset.model
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(model.__name__)
    writer = csv.writer(response)
    model_admin = admin.site._registry[model]
    list_display = model_admin.list_display 
    # Write headers to CSV file
    if list_display and len(list_display) > 0:
        headers = list_display[1:]
    else:
        headers = []
        for field in model._meta.fields:
            headers.append(field.name)
    writer.writerow(headers)
    # Write data to CSV file
    for obj in queryset:
        row = []
        for field in headers:
            if field in headers:
                try:
                    val = getattr(obj, field)
                    if callable(val):
                        val = val()
                except AttributeError:
                    val = getattr(admin.site._registry[model], field)
                    if callable(val):
                        val = val(obj)
                row.append(val)
        writer.writerow(row)
    # Return CSV file to browser as download
    return response