from django.contrib import admin
from comdb.models import userinfo,question,Choice

# Register your models here.
class userinfoAdmin(admin.ModelAdmin):
    list_display = ['name','email','password','addr']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class questioinAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']
    readonly_fields = ('pub_date',)

admin.site.register(userinfo,userinfoAdmin)
admin.site.register(question,questioinAdmin)