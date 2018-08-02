from django.contrib import admin
from comdb.models import userinfo

# Register your models here.
class userinfoAdmin(admin.ModelAdmin):
    list_display = ['name','email','addr']

admin.site.register(userinfo,userinfoAdmin)