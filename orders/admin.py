from django.contrib import admin
from .models import Order,OrderItem,OrderPay
import csv
import datetime
from django.http import HttpResponse


def export_to_csv(modeladmin,request,queryset):
    opts=modeladmin.model._meta
    content_disposition=f'attachment;filename={opts.verbose_name}.csv'
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']=content_disposition

    writer=csv.writer(response)
    #row in excelsheet without relation one to many or many to many 
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow(field.verbose_name for field in fields)

    for obj in queryset:
        date_row = []
        for field in fields:
            value=getattr(obj,field.name)
            if isinstance(value,datetime.datetime):
                value=value.strftime('%d%m%Y')
            date_row.append(value)
        writer.writerow(date_row)
    return response


export_to_csv.short_description='Export to CSV'


class OrderItemInline(admin.TabularInline):   #TabularInline => OrderAdminيظهر تحت جدول ال 
    model=OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['first_name','email','paid','created_at']
    inlines=[OrderItemInline]
    actions=[export_to_csv]

