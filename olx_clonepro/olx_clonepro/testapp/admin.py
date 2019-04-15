from django.contrib import admin
from .models import UserSellingData

class UserSellingAdmin(admin.ModelAdmin):
    list_display = ['bike_name','product_id','bike_price','bike_old','bike_desc','bike_img','currdata']

admin.site.register(UserSellingData,UserSellingAdmin)
