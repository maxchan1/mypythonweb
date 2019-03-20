from django.contrib import admin
from comdb.models import userinfo,question,Choice

# Register your models here.
class userinfoAdmin(admin.ModelAdmin):
    list_display = ['name','email','password','addr']

    actions = ['make_published']  # 请注意这里改成字符串引用了

    def make_published(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        print(selected)
        self.message_user(request,"请根据选择了附件爱疯")

    make_published.short_description = "Mark selected stories as published"

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