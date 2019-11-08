from django import forms

class uploadfileform(forms.Form):
    titlep = forms.CharField(label="表单名称",max_length=50)
    #file = forms.FileField()